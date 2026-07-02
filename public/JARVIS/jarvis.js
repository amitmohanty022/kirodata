/* ==================================================================
 *  J.A.R.V.I.S.  —  voice-enabled personal assistant
 *  - Offline: time, date, math, jokes, profile, system commands
 *  - Online : web search, Wikipedia answers, weather, YouTube play
 *  Pure client-side. No backend, no API keys required.
 * ================================================================== */
(() => {
  "use strict";

  const OWNER = window.OWNER || { firstName: "sir", honorific: "sir" };
  const $ = (id) => document.getElementById(id);

  /* ---------- persisted settings ---------- */
  const store = {
    get(k, d) { try { const v = localStorage.getItem("jarvis_" + k); return v === null ? d : JSON.parse(v); } catch { return d; } },
    set(k, v) { try { localStorage.setItem("jarvis_" + k, JSON.stringify(v)); } catch {} },
  };
  const settings = {
    voiceURI: store.get("voiceURI", null),
    rate: store.get("rate", 1.0),
    pitch: store.get("pitch", 0.9),
    wake: store.get("wake", false),
    tts: store.get("tts", true),
    owner: store.get("owner", OWNER.firstName || "sir"),
  };

  /* ================= Speech synthesis ================= */
  const synth = window.speechSynthesis;
  let voices = [];
  let speaking = false;

  function loadVoices() {
    voices = synth ? synth.getVoices() : [];
    const sel = $("voiceSelect");
    if (!sel) return;
    sel.innerHTML = "";
    voices.forEach((v) => {
      const o = document.createElement("option");
      o.value = v.voiceURI;
      o.textContent = `${v.name} (${v.lang})`;
      sel.appendChild(o);
    });
    if (!settings.voiceURI) settings.voiceURI = pickDefaultVoice();
    if (settings.voiceURI) sel.value = settings.voiceURI;
  }

  // Prefer a crisp British male voice to approximate the JARVIS vibe.
  function pickDefaultVoice() {
    if (!voices.length) return null;
    const score = (v) => {
      let s = 0;
      const n = v.name.toLowerCase();
      if (/en-gb/i.test(v.lang)) s += 6;
      if (/\bgb\b|british|uk/i.test(n)) s += 4;
      if (/daniel|george|arthur|oliver|james|ryan|male/i.test(n)) s += 5;
      if (/google uk english male/i.test(n)) s += 8;
      if (/microsoft (ryan|george|thomas)/i.test(n)) s += 6;
      if (/en-/i.test(v.lang)) s += 1;
      if (/female|zira|samantha|hazel/i.test(n)) s -= 3;
      return s;
    };
    return [...voices].sort((a, b) => score(b) - score(a))[0].voiceURI;
  }

  function currentVoice() {
    return voices.find((v) => v.voiceURI === settings.voiceURI) || voices[0] || null;
  }

  function speak(text, onEnd) {
    if (!settings.tts || !synth) { onEnd && onEnd(); return; }
    try { synth.cancel(); } catch {}
    const u = new SpeechSynthesisUtterance(text.replace(/<[^>]+>/g, ""));
    const v = currentVoice();
    if (v) { u.voice = v; u.lang = v.lang; }
    u.rate = settings.rate;
    u.pitch = settings.pitch;
    u.onstart = () => { speaking = true; setReactor("speaking"); };
    u.onend = () => { speaking = false; setReactor(recognizing ? "listening" : "idle"); onEnd && onEnd(); };
    u.onerror = () => { speaking = false; setReactor(recognizing ? "listening" : "idle"); onEnd && onEnd(); };
    synth.speak(u);
  }

  if (synth) {
    loadVoices();
    synth.onvoiceschanged = loadVoices;
  }

  /* ================= Conversation log ================= */
  const log = $("log");
  function addMsg(text, who) {
    const d = document.createElement("div");
    d.className = "msg " + who;
    d.innerHTML = text;
    log.appendChild(d);
    log.scrollTop = log.scrollHeight;
    return d;
  }
  function jarvisSay(text, opts = {}) {
    addMsg(text, "jarvis");
    speak(opts.spoken || text);
  }

  /* ================= Network status ================= */
  function isOnline() { return navigator.onLine; }
  function refreshNet() {
    const on = isOnline();
    $("netDot").classList.toggle("on", on);
    $("netText").textContent = on ? "ONLINE" : "OFFLINE";
  }
  window.addEventListener("online", refreshNet);
  window.addEventListener("offline", refreshNet);

  /* ================= Reactor visualizer ================= */
  const rc = $("reactor");
  const rx = rc.getContext("2d");
  let mode = "idle"; // idle | listening | speaking | thinking
  let t = 0;
  function setReactor(m) { mode = m; $("reactorCaption").textContent =
    m === "listening" ? "LISTENING…" : m === "speaking" ? "SPEAKING" : m === "thinking" ? "PROCESSING" : "STANDING BY"; }

  function drawReactor() {
    const w = rc.width, h = rc.height, cx = w / 2, cy = h / 2;
    rx.clearRect(0, 0, w, h);
    const base = mode === "speaking" ? 0.5 + Math.abs(Math.sin(t * 0.18)) * 0.5
               : mode === "listening" ? 0.4 + Math.abs(Math.sin(t * 0.09)) * 0.3
               : mode === "thinking" ? 0.6 : 0.32;
    const col = mode === "listening" ? "0,234,255" : mode === "thinking" ? "255,179,71" : "0,234,255";

    // outer rotating ticks
    for (let i = 0; i < 60; i++) {
      const a = (i / 60) * Math.PI * 2 + t * 0.004;
      const r1 = 230, r2 = 230 + (i % 5 === 0 ? 18 : 9);
      rx.strokeStyle = `rgba(${col},${0.15 + (i % 5 === 0 ? 0.25 : 0)})`;
      rx.lineWidth = i % 5 === 0 ? 2 : 1;
      rx.beginPath();
      rx.moveTo(cx + Math.cos(a) * r1, cy + Math.sin(a) * r1);
      rx.lineTo(cx + Math.cos(a) * r2, cy + Math.sin(a) * r2);
      rx.stroke();
    }
    // rotating arcs
    [ [200, 0.005, 0, 1.6], [175, -0.008, 2, 1.2], [150, 0.011, 4, 2.0] ].forEach(([r, sp, off, len]) => {
      rx.strokeStyle = `rgba(${col},0.5)`;
      rx.lineWidth = 2;
      rx.beginPath();
      rx.arc(cx, cy, r, t * sp + off, t * sp + off + len);
      rx.stroke();
    });
    // pulsing core rings
    for (let k = 0; k < 4; k++) {
      const r = 40 + k * 22 + Math.sin(t * 0.08 + k) * 4;
      rx.strokeStyle = `rgba(${col},${0.6 - k * 0.12})`;
      rx.lineWidth = 2;
      rx.beginPath(); rx.arc(cx, cy, r, 0, Math.PI * 2); rx.stroke();
    }
    // glowing core
    const g = rx.createRadialGradient(cx, cy, 0, cx, cy, 60 * base + 30);
    g.addColorStop(0, `rgba(${col},${0.9 * base + 0.1})`);
    g.addColorStop(0.6, `rgba(${col},${0.25 * base})`);
    g.addColorStop(1, "rgba(0,0,0,0)");
    rx.fillStyle = g;
    rx.beginPath(); rx.arc(cx, cy, 60 * base + 30, 0, Math.PI * 2); rx.fill();

    t++;
    requestAnimationFrame(drawReactor);
  }
  drawReactor();

  /* ================= Background particles ================= */
  const bg = $("bg"), bx = bg.getContext("2d");
  let pts = [];
  function resizeBg() {
    bg.width = innerWidth; bg.height = innerHeight;
    pts = Array.from({ length: Math.min(90, Math.floor(innerWidth / 16)) }, () => ({
      x: Math.random() * bg.width, y: Math.random() * bg.height,
      vx: (Math.random() - 0.5) * 0.3, vy: (Math.random() - 0.5) * 0.3,
    }));
  }
  function drawBg() {
    bx.clearRect(0, 0, bg.width, bg.height);
    bx.fillStyle = "rgba(0,234,255,0.5)";
    pts.forEach((p) => {
      p.x += p.vx; p.y += p.vy;
      if (p.x < 0 || p.x > bg.width) p.vx *= -1;
      if (p.y < 0 || p.y > bg.height) p.vy *= -1;
      bx.beginPath(); bx.arc(p.x, p.y, 1.1, 0, Math.PI * 2); bx.fill();
    });
    for (let i = 0; i < pts.length; i++)
      for (let j = i + 1; j < pts.length; j++) {
        const dx = pts[i].x - pts[j].x, dy = pts[i].y - pts[j].y;
        const d = Math.hypot(dx, dy);
        if (d < 120) {
          bx.strokeStyle = `rgba(0,234,255,${0.12 * (1 - d / 120)})`;
          bx.beginPath(); bx.moveTo(pts[i].x, pts[i].y); bx.lineTo(pts[j].x, pts[j].y); bx.stroke();
        }
      }
    requestAnimationFrame(drawBg);
  }
  addEventListener("resize", resizeBg);
  resizeBg();
  drawBg();

  /* ================= Speech recognition ================= */
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  let recognition = null;
  let recognizing = false;
  let manualStop = false;

  function buildRecognition() {
    if (!SR) return null;
    const r = new SR();
    r.continuous = true;
    r.interimResults = true;
    r.lang = "en-US";
    r.onstart = () => {
      recognizing = true;
      $("micDot").className = "dot live";
      $("micText").textContent = "LISTENING";
      $("micBtn").classList.add("live");
      if (!speaking) setReactor("listening");
    };
    r.onerror = (e) => {
      if (e.error === "not-allowed" || e.error === "service-not-allowed") {
        jarvisSay("I could not access the microphone. Please grant mic permission, or type to me instead.");
        manualStop = true;
      }
    };
    r.onend = () => {
      recognizing = false;
      $("micDot").className = "dot dot-idle";
      $("micText").textContent = "MIC IDLE";
      $("micBtn").classList.remove("live");
      if (!speaking) setReactor("idle");
      // keep listening in hands-free mode
      if (settings.wake && !manualStop) { try { r.start(); } catch {} }
    };
    r.onresult = (e) => {
      let interim = "", final = "";
      for (let i = e.resultIndex; i < e.results.length; i++) {
        const tr = e.results[i][0].transcript;
        if (e.results[i].isFinal) final += tr; else interim += tr;
      }
      $("interim").textContent = interim;
      if (final.trim()) {
        $("interim").textContent = "";
        handleSpeech(final.trim());
      }
    };
    return r;
  }

  function startListening(manual) {
    if (!SR) { jarvisSay("Speech recognition is not supported in this browser. Try Chrome or Edge, or type your command."); return; }
    manualStop = false;
    if (!recognition) recognition = buildRecognition();
    try { recognition.start(); } catch {}
  }
  function stopListening() {
    manualStop = true;
    if (recognition) { try { recognition.stop(); } catch {} }
  }

  // In hands-free mode we require the wake word; in manual mode we don't.
  function handleSpeech(text) {
    if (settings.wake) {
      const m = text.match(/\b(jarvis|hey jarvis|ok jarvis)\b[\s,!.:-]*(.*)/i);
      if (!m) return; // ignore chatter without wake word
      const cmd = (m[2] || "").trim();
      if (!cmd) { addMsg(text, "user"); jarvisSay(`Yes, ${settings.owner}?`); return; }
      addMsg(cmd, "user");
      route(cmd);
    } else {
      addMsg(text, "user");
      route(text);
    }
  }

  /* ================= Command brain ================= */
  function greeting() {
    const h = new Date().getHours();
    return h < 12 ? "Good morning" : h < 18 ? "Good afternoon" : "Good evening";
  }
  const owner = () => settings.owner || "sir";

  function route(raw) {
    const text = raw.trim();
    const q = text.toLowerCase();
    setReactor("thinking");

    /* ---- conversational ---- */
    if (/^(hi|hello|hey|yo|greetings)\b/.test(q))
      return jarvisSay(`${greeting()}, ${owner()}. JARVIS online and at your service. How may I help?`);
    if (/how are you|how('?| a)re you doing|what'?s up/.test(q))
      return jarvisSay(`All systems nominal, ${owner()}. Standing by for your command.`);
    if (/who are you|what are you|your name/.test(q))
      return jarvisSay("I am JARVIS — Just A Rather Very Intelligent System — your personal assistant.");
    if (/thank you|thanks|thank u|cheers/.test(q))
      return jarvisSay(`Always a pleasure, ${owner()}.`);
    if (/who (made|created|built) you|who is your (creator|developer)/.test(q))
      return jarvisSay(`I was configured for ${OWNER.name}. Consider me your personal system.`);

    /* ---- time / date ---- */
    if (/\b(time|what time)\b/.test(q) && !/timer/.test(q)) {
      const now = new Date();
      return jarvisSay(`It is ${now.toLocaleTimeString([], { hour: "numeric", minute: "2-digit" })}, ${owner()}.`);
    }
    if (/\b(date|day|today)\b/.test(q) && !/birthday/.test(q)) {
      const now = new Date();
      return jarvisSay(`Today is ${now.toLocaleDateString([], { weekday: "long", year: "numeric", month: "long", day: "numeric" })}.`);
    }

    /* ---- timer ---- */
    const tm = q.match(/(?:set|start)?\s*(?:a\s*)?timer\s*(?:for\s*)?(\d+)\s*(second|sec|minute|min|hour|hr)/);
    if (tm) {
      const n = +tm[1];
      const unit = tm[2];
      const ms = n * (/(hour|hr)/.test(unit) ? 3600000 : /(min)/.test(unit) ? 60000 : 1000);
      jarvisSay(`Timer set for ${n} ${unit}${n > 1 ? "s" : ""}, ${owner()}.`);
      setTimeout(() => jarvisSay(`${owner()}, your ${n} ${unit} timer has elapsed.`), ms);
      return;
    }

    /* ---- math ---- */
    if (/[0-9]/.test(q) && /(\+|-|\*|\/|plus|minus|times|divided|multipl|x )|what is \d/.test(q)) {
      const r = tryMath(q);
      if (r !== null) return jarvisSay(`That is ${r}, ${owner()}.`);
    }

    /* ---- profile / "know me" ---- */
    const p = profileAnswer(q);
    if (p) return jarvisSay(p);

    /* ---- jokes ---- */
    if (/joke|make me laugh|funny/.test(q)) return jarvisSay(randomJoke());

    /* ---- open sites ---- */
    const openM = q.match(/^open\s+(.+)/) || q.match(/launch\s+(.+)/);
    if (openM) return openSite(openM[1].trim());

    /* ---- settings via voice ---- */
    if (/(stop|be quiet|silence|shut up)/.test(q)) { synth && synth.cancel(); return; }
    if (/full ?screen/.test(q)) { toggleFullscreen(); return jarvisSay("Engaging fullscreen."); }

    /* ====================== ONLINE features ====================== */
    // play music / video on youtube
    const playM = q.match(/(?:play|put on|start)\s+(.+?)(?:\s+(?:on|in|from)\s+youtube)?$/);
    if (playM && /(play|put on)/.test(q) && !/playlist of nothing/.test(q)) {
      return playMedia(playM[1].replace(/\bsong\b|\bmusic\b|\bvideo\b/g, "").trim() || playM[1].trim());
    }
    // weather
    const wM = q.match(/weather(?:\s+(?:in|at|for))?\s+(.+)/) || (/(weather|temperature)/.test(q) ? { 1: "" } : null);
    if (wM) return getWeather((wM[1] || OWNER.location || "").replace(/[?.!]/g, "").trim());
    // wiki / who is / what is / tell me about
    const wikiM = q.match(/^(?:who is|who was|what is|what are|what's|tell me about|define|explain)\s+(.+)/);
    if (wikiM) return wikiAnswer(wikiM[1].replace(/[?.!]/g, "").trim());
    // explicit search
    const sM = q.match(/^(?:search|google|look up|find)\s+(?:for\s+)?(.+)/);
    if (sM) return webSearch(sM[1].replace(/[?.!]/g, "").trim());
    // news
    if (/\bnews\b|headlines/.test(q)) { openURL("https://news.google.com/"); return jarvisSay("Pulling up the latest headlines, " + owner() + "."); }

    /* ---- fallback ---- */
    if (isOnline()) {
      jarvisSay(`I am not certain, ${owner()} — let me search the web for that.`);
      return wikiAnswer(text, true);
    }
    return jarvisSay(`I did not quite catch a command in that, ${owner()}. I can handle time, date, math, jokes, your profile, and system tasks offline — and search, weather, and music when you are online.`);
  }

  /* ---------- math ---------- */
  function tryMath(q) {
    let s = q
      .replace(/what is|what's|calculate|compute|equals?|how much is/g, " ")
      .replace(/plus/g, "+").replace(/minus/g, "-")
      .replace(/times|multiplied by|x/g, "*").replace(/divided by|over/g, "/")
      .replace(/[^0-9+\-*/.() ]/g, " ").trim();
    if (!/[0-9]/.test(s) || !/[+\-*/]/.test(s)) return null;
    try {
      if (!/^[0-9+\-*/.() ]+$/.test(s)) return null;
      const r = Function('"use strict";return (' + s + ")")();
      return (typeof r === "number" && isFinite(r)) ? +r.toFixed(6) / 1 : null;
    } catch { return null; }
  }

  /* ---------- jokes (offline) ---------- */
  const JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "There are 10 types of people in the world — those who understand binary, and those who do not.",
    "I would tell you a UDP joke, but you might not get it.",
    "A SQL query walks into a bar, approaches two tables, and asks: may I join you?",
    "Why did the neural network break up? It had too many hidden layers of issues.",
    "I told my computer I needed a break, and now it will not stop sending me Kit-Kat ads.",
  ];
  function randomJoke() { return JOKES[Math.floor(Math.random() * JOKES.length)]; }

  /* ---------- profile answers ---------- */
  function profileAnswer(q) {
    const me = OWNER;
    if (/who am i|about me|tell me about myself|my profile|my bio/.test(q))
      return `You are ${me.name}, ${me.roles[0]} based in ${me.location}. ${me.summary}`;
    if (/my name|what'?s my name/.test(q)) return `You are ${me.name}, ${owner()}.`;
    if (/my (email|e-mail)/.test(q)) return `Your email is ${me.email}.`;
    if (/my (phone|number|contact)/.test(q)) return `Your phone number is ${me.phone}.`;
    if (/my (github|git hub)/.test(q)) { openURL(me.github); return `Opening your GitHub profile, ${owner()}: ${me.github}`; }
    if (/my linkedin/.test(q)) { openURL(me.linkedin); return `Opening your LinkedIn, ${owner()}.`; }
    if (/my (location|city|where (do|am) i)/.test(q)) return `You are based in ${me.location}.`;
    if (/my (skills|tech stack|technolog)/.test(q)) {
      const all = Object.entries(me.skills).map(([k, v]) => `${k}: ${v.slice(0, 6).join(", ")}`).join(". ");
      return `Your core skills — ${all}.`;
    }
    if (/my (experience|work|job|career)/.test(q)) {
      const e = me.experience[0];
      return `You currently work as ${e.role} at ${e.company} since ${e.period.split(" to ")[0]}. ${e.note}`;
    }
    if (/my (projects|portfolio work)/.test(q))
      return "Your headline projects are: " + me.projects.map((p) => p.title).join("; ") + ". Ask me about any one of them.";
    me.projects.forEach(() => {});
    for (const pr of me.projects) {
      const key = pr.title.toLowerCase().split(" ")[0];
      if (q.includes(key) && /project|tell|about|explain|what/.test(q)) return `${pr.title}: ${pr.note}`;
    }
    if (/my (education|college|university|degree|study)/.test(q))
      return `You studied at ${me.education.institution}, completing a ${me.education.degree} from ${me.education.period}. ${me.education.detail}`;
    if (/my (achievement|award|accomplishment)/.test(q))
      return "Your achievements include: " + me.achievements.join(" ");
    if (/(rookie of the year|award)/.test(q) && /my|me/.test(q))
      return me.achievements[0];
    return null;
  }

  /* ---------- open sites ---------- */
  function openSite(name) {
    const map = {
      youtube: "https://youtube.com", google: "https://google.com", gmail: "https://mail.google.com",
      github: OWNER.github, linkedin: OWNER.linkedin, twitter: "https://twitter.com", x: "https://x.com",
      maps: "https://maps.google.com", spotify: "https://open.spotify.com", whatsapp: "https://web.whatsapp.com",
      chatgpt: "https://chat.openai.com", instagram: "https://instagram.com", netflix: "https://netflix.com",
      reddit: "https://reddit.com", stackoverflow: "https://stackoverflow.com",
    };
    const key = Object.keys(map).find((k) => name.includes(k));
    if (key) { openURL(map[key]); return jarvisSay(`Opening ${key}, ${owner()}.`); }
    if (!isOnline()) return jarvisSay(`I need an internet connection to open ${name}, ${owner()}.`);
    // try as a domain or search
    const guess = name.replace(/\s+/g, "");
    const url = /\./.test(guess) ? "https://" + guess.replace(/^https?:\/\//, "") : null;
    if (url) { openURL(url); return jarvisSay(`Opening ${name}.`); }
    return webSearch(name);
  }

  /* ================= ONLINE: media playback ================= */
  function playMedia(query) {
    if (!isOnline()) return jarvisSay(`I cannot reach YouTube while offline, ${owner()}. Connect to the internet and try again.`);
    jarvisSay(`Now playing ${query}, ${owner()}.`);
    // Use YouTube's embed playlist search to autoplay the top result.
    const frame = `<iframe src="https://www.youtube.com/embed?listType=search&list=${encodeURIComponent(query)}&autoplay=1" allow="autoplay; encrypted-media" allowfullscreen></iframe>`;
    $("mediaTitle").textContent = "NOW PLAYING — " + query.toUpperCase();
    $("mediaBody").innerHTML = frame;
    $("media").hidden = false;
    // Fallback link in case embedding is blocked.
    addMsg(`If playback does not start, <a href="https://www.youtube.com/results?search_query=${encodeURIComponent(query)}" target="_blank" rel="noopener">open it on YouTube</a>.`, "jarvis");
  }

  /* ================= ONLINE: Wikipedia ================= */
  async function wikiAnswer(topic, quiet) {
    if (!isOnline()) return jarvisSay(`That requires the internet, ${owner()}, and we are currently offline.`);
    if (!quiet) { addMsg(`Searching for <b>${escapeHtml(topic)}</b>…`, "jarvis"); }
    try {
      const r = await fetch("https://en.wikipedia.org/api/rest_v1/page/summary/" + encodeURIComponent(topic), { headers: { accept: "application/json" } });
      if (!r.ok) throw new Error("not found");
      const d = await r.json();
      if (d.type && d.type.includes("disambiguation")) throw new Error("disambig");
      if (d.extract) {
        const more = d.content_urls && d.content_urls.desktop ? ` <a href="${d.content_urls.desktop.page}" target="_blank" rel="noopener">Read more</a>.` : "";
        addMsg(d.extract + more, "jarvis");
        return speak(d.extract.split(". ").slice(0, 2).join(". ") + ".");
      }
      throw new Error("empty");
    } catch {
      jarvisSay(`I could not find a clear answer for that, ${owner()}. Let me run a web search.`, {});
      return webSearch(topic);
    }
  }

  /* ================= ONLINE: web search ================= */
  function webSearch(query) {
    if (!isOnline()) return jarvisSay(`I need internet access to search, ${owner()}.`);
    const url = "https://www.google.com/search?q=" + encodeURIComponent(query);
    openURL(url);
    addMsg(`Searching the web for <a href="${url}" target="_blank" rel="noopener">${escapeHtml(query)}</a>.`, "jarvis");
    speak(`Searching the web for ${query}, ${owner()}.`);
  }

  /* ================= ONLINE: weather (Open-Meteo, no key) ================= */
  async function getWeather(place) {
    if (!isOnline()) return jarvisSay(`Weather data needs an internet connection, ${owner()}.`);
    const city = place || OWNER.location || "Gurgaon";
    addMsg(`Fetching the weather for <b>${escapeHtml(city)}</b>…`, "jarvis");
    try {
      const g = await fetch("https://geocoding-api.open-meteo.com/v1/search?count=1&name=" + encodeURIComponent(city));
      const gd = await g.json();
      if (!gd.results || !gd.results.length) throw new Error("nogeo");
      const { latitude, longitude, name, country } = gd.results[0];
      const w = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m`);
      const wd = await w.json();
      const c = wd.current;
      const desc = weatherCode(c.weather_code);
      const msg = `In ${name}${country ? ", " + country : ""} it is currently ${Math.round(c.temperature_2m)}°C with ${desc}, humidity ${c.relative_humidity_2m}% and wind ${Math.round(c.wind_speed_10m)} km/h.`;
      jarvisSay(msg);
    } catch {
      jarvisSay(`I was unable to retrieve the weather for ${city}, ${owner()}.`);
    }
  }
  function weatherCode(code) {
    const m = { 0: "clear skies", 1: "mostly clear", 2: "partly cloudy", 3: "overcast", 45: "fog", 48: "freezing fog", 51: "light drizzle", 61: "light rain", 63: "rain", 65: "heavy rain", 71: "light snow", 73: "snow", 75: "heavy snow", 80: "rain showers", 95: "thunderstorms", 96: "thunderstorms with hail" };
    return m[code] || "variable conditions";
  }

  /* ---------- helpers ---------- */
  function openURL(u) { try { window.open(u, "_blank", "noopener"); } catch {} }
  function escapeHtml(s) { return String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c])); }
  function toggleFullscreen() { if (!document.fullscreenElement) document.documentElement.requestFullscreen?.(); else document.exitFullscreen?.(); }

  /* ================= UI wiring ================= */
  $("inputForm").addEventListener("submit", (e) => {
    e.preventDefault();
    const v = $("textInput").value.trim();
    if (!v) return;
    $("textInput").value = "";
    addMsg(v, "user");
    route(v);
  });

  let pressTimer = null;
  $("micBtn").addEventListener("click", () => {
    if (recognizing) stopListening(); else startListening(true);
  });

  $("wakeToggle").addEventListener("click", () => setWake(!settings.wake));
  function setWake(on) {
    settings.wake = on; store.set("wake", on);
    $("wakeChk").checked = on;
    $("wakeToggle").classList.toggle("active", on);
    $("wakeToggle").textContent = on ? "WAKE: ON" : "WAKE: JARVIS";
    if (on) { jarvisSay(`Hands-free mode engaged. Say "Jarvis" followed by your command.`); startListening(false); }
    else { stopListening(); }
  }

  // settings drawer
  $("settingsBtn").addEventListener("click", () => { $("settings").hidden = false; });
  $("settingsClose").addEventListener("click", () => { $("settings").hidden = true; });
  $("voiceSelect").addEventListener("change", (e) => { settings.voiceURI = e.target.value; store.set("voiceURI", settings.voiceURI); });
  $("rate").addEventListener("input", (e) => { settings.rate = +e.target.value; $("rateVal").textContent = settings.rate.toFixed(2); store.set("rate", settings.rate); });
  $("pitch").addEventListener("input", (e) => { settings.pitch = +e.target.value; $("pitchVal").textContent = settings.pitch.toFixed(2); store.set("pitch", settings.pitch); });
  $("wakeChk").addEventListener("change", (e) => setWake(e.target.checked));
  $("ttsChk").addEventListener("change", (e) => { settings.tts = e.target.checked; store.set("tts", settings.tts); });
  $("ownerName").addEventListener("input", (e) => { settings.owner = e.target.value.trim() || OWNER.firstName; store.set("owner", settings.owner); });
  $("testVoice").addEventListener("click", () => speak(`${greeting()}, ${owner()}. Voice systems are online and calibrated.`));
  $("mediaClose").addEventListener("click", () => { $("media").hidden = true; $("mediaBody").innerHTML = ""; });

  // init settings UI
  $("rate").value = settings.rate; $("rateVal").textContent = settings.rate.toFixed(2);
  $("pitch").value = settings.pitch; $("pitchVal").textContent = settings.pitch.toFixed(2);
  $("ttsChk").checked = settings.tts;
  $("wakeChk").checked = settings.wake;
  $("ownerName").value = settings.owner;
  $("wakeToggle").classList.toggle("active", settings.wake);
  $("wakeToggle").textContent = settings.wake ? "WAKE: ON" : "WAKE: JARVIS";
  refreshNet();

  /* ================= Boot sequence ================= */
  const bootLines = [
    "> initializing J.A.R.V.I.S. kernel ...",
    "> loading natural-language interface ......... OK",
    "> calibrating speech synthesis ............... OK",
    "> mounting offline command core .............. OK",
    `> network uplink: ${isOnline() ? "DETECTED" : "OFFLINE MODE"}`,
    `> operator profile: ${OWNER.name} ............ LOADED`,
    "> all systems nominal.",
  ];
  const bootLog = $("bootLog");
  let bi = 0;
  function typeBoot() {
    if (bi < bootLines.length) {
      bootLog.textContent += bootLines[bi++] + "\n";
      setTimeout(typeBoot, 360);
    } else {
      $("bootBtn").hidden = false;
    }
  }
  typeBoot();
  $("bootBtn").addEventListener("click", () => {
    $("boot").classList.add("hide");
    setTimeout(() => { $("boot").style.display = "none"; }, 600);
    // greeting + (browser requires a user gesture before audio/mic — this is it)
    jarvisSay(`${greeting()}, ${owner()}. JARVIS is online. ${SR ? "" : "Note: voice input is not supported in this browser, but you can type to me."} How may I assist you today?`);
    if (settings.wake && SR) setTimeout(() => startListening(false), 1200);
  });
})();
