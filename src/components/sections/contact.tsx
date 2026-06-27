"use client";

import { useRef, useState, type FormEvent } from "react";
import emailjs from "@emailjs/browser";
import { motion } from "framer-motion";
import { CheckCircle2, Loader2, Mail, MapPin, Phone, Send } from "lucide-react";
import { profile } from "@/lib/data";
import { Section } from "@/components/ui/section";
import { SocialLinks } from "@/components/ui/social-links";

type Status = "idle" | "sending" | "success" | "error";

export function Contact() {
  const formRef = useRef<HTMLFormElement>(null);
  const [status, setStatus] = useState<Status>("idle");
  const [error, setError] = useState("");

  const serviceId = process.env.NEXT_PUBLIC_EMAILJS_SERVICE_ID;
  const templateId = process.env.NEXT_PUBLIC_EMAILJS_TEMPLATE_ID;
  const publicKey = process.env.NEXT_PUBLIC_EMAILJS_PUBLIC_KEY;
  const emailjsReady = Boolean(serviceId && templateId && publicKey);

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    if (!formRef.current) return;

    // Graceful fallback when EmailJS isn't configured: open the user's mail client.
    if (!emailjsReady) {
      const data = new FormData(formRef.current);
      const subject = encodeURIComponent(
        `Portfolio message from ${data.get("from_name") ?? ""}`
      );
      const body = encodeURIComponent(
        `${data.get("message") ?? ""}\n\nFrom: ${data.get("from_name") ?? ""} (${
          data.get("reply_to") ?? ""
        })`
      );
      window.location.href = `mailto:${profile.email}?subject=${subject}&body=${body}`;
      return;
    }

    setStatus("sending");
    setError("");
    try {
      await emailjs.sendForm(
        serviceId!,
        templateId!,
        formRef.current,
        publicKey!
      );
      setStatus("success");
      formRef.current.reset();
    } catch (err) {
      console.error(err);
      setStatus("error");
      setError("Something went wrong. Please email me directly.");
    }
  }

  const contactDetails = [
    { icon: Mail, label: "Email", value: profile.email, href: `mailto:${profile.email}` },
    { icon: Phone, label: "Phone", value: profile.phone, href: "tel:+919354937256" },
    { icon: MapPin, label: "Location", value: profile.location },
  ];

  return (
    <Section
      id="contact"
      eyebrow="Contact"
      title={<>Let&apos;s build something <span className="gradient-text">together</span></>}
      description="Have a role, project, or idea in mind? My inbox is always open."
    >
      <div className="mx-auto grid max-w-5xl gap-8 lg:grid-cols-[1fr_1.3fr]">
        {/* Info */}
        <div className="space-y-6">
          <div className="card-surface glow-border space-y-5 p-6">
            {contactDetails.map((item) => {
              const Icon = item.icon;
              const content = (
                <>
                  <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-lg bg-primary/10 text-primary">
                    <Icon className="h-5 w-5" />
                  </span>
                  <span className="min-w-0">
                    <span className="block text-xs uppercase tracking-wide text-muted-foreground">
                      {item.label}
                    </span>
                    <span className="block truncate font-medium">{item.value}</span>
                  </span>
                </>
              );
              return item.href ? (
                <a
                  key={item.label}
                  href={item.href}
                  className="flex items-center gap-4 transition-colors hover:text-primary"
                >
                  {content}
                </a>
              ) : (
                <div key={item.label} className="flex items-center gap-4">
                  {content}
                </div>
              );
            })}
          </div>
          <div className="card-surface p-6">
            <p className="mb-4 text-sm font-medium text-muted-foreground">
              Find me online
            </p>
            <SocialLinks />
          </div>
        </div>

        {/* Form */}
        <motion.div
          initial={{ opacity: 0, y: 24 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5 }}
          className="card-surface glow-border p-6 sm:p-8"
        >
          {status === "success" ? (
            <div className="flex flex-col items-center justify-center py-12 text-center">
              <CheckCircle2 className="mb-4 h-14 w-14 text-emerald-500" />
              <h3 className="text-xl font-bold">Message sent!</h3>
              <p className="mt-2 text-muted-foreground">
                Thanks for reaching out — I&apos;ll get back to you soon.
              </p>
              <button
                type="button"
                onClick={() => setStatus("idle")}
                className="mt-6 rounded-full border border-border px-5 py-2 text-sm font-medium hover:border-primary/50 hover:text-primary"
              >
                Send another
              </button>
            </div>
          ) : (
            <form ref={formRef} onSubmit={handleSubmit} className="space-y-5">
              <div className="grid gap-5 sm:grid-cols-2">
                <Field label="Name" htmlFor="from_name">
                  <input
                    id="from_name"
                    name="from_name"
                    type="text"
                    required
                    autoComplete="name"
                    placeholder="Your name"
                    className="form-input"
                  />
                </Field>
                <Field label="Email" htmlFor="reply_to">
                  <input
                    id="reply_to"
                    name="reply_to"
                    type="email"
                    required
                    autoComplete="email"
                    placeholder="you@example.com"
                    className="form-input"
                  />
                </Field>
              </div>
              <Field label="Message" htmlFor="message">
                <textarea
                  id="message"
                  name="message"
                  required
                  rows={5}
                  placeholder="Tell me about your project or opportunity..."
                  className="form-input resize-none"
                />
              </Field>

              {status === "error" && (
                <p className="text-sm text-red-500" role="alert">
                  {error}
                </p>
              )}
              {!emailjsReady && (
                <p className="text-xs text-muted-foreground">
                  Tip: configure EmailJS env vars to send in-app; otherwise this
                  opens your mail client.
                </p>
              )}

              <button
                type="submit"
                disabled={status === "sending"}
                className="inline-flex w-full items-center justify-center gap-2 rounded-xl bg-primary px-6 py-3 font-semibold text-primary-foreground shadow-lg shadow-primary/30 transition-transform hover:scale-[1.02] disabled:cursor-not-allowed disabled:opacity-70"
              >
                {status === "sending" ? (
                  <>
                    <Loader2 className="h-4 w-4 animate-spin" />
                    Sending...
                  </>
                ) : (
                  <>
                    <Send className="h-4 w-4" />
                    Send Message
                  </>
                )}
              </button>
            </form>
          )}
        </motion.div>
      </div>
    </Section>
  );
}

function Field({
  label,
  htmlFor,
  children,
}: {
  label: string;
  htmlFor: string;
  children: React.ReactNode;
}) {
  return (
    <label htmlFor={htmlFor} className="block">
      <span className="mb-1.5 block text-sm font-medium">{label}</span>
      {children}
    </label>
  );
}
