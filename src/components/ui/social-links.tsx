import { Github, Linkedin, Mail, Phone } from "lucide-react";
import { socials, type SocialLink } from "@/lib/data";
import { cn } from "@/lib/utils";

const iconMap = {
  github: Github,
  linkedin: Linkedin,
  mail: Mail,
  phone: Phone,
};

export function SocialLinks({ className }: { className?: string }) {
  return (
    <ul className={cn("flex items-center gap-3", className)}>
      {socials.map((social: SocialLink) => {
        const Icon = iconMap[social.icon];
        const isExternal = social.href.startsWith("http");
        return (
          <li key={social.label}>
            <a
              href={social.href}
              aria-label={social.label}
              title={social.label}
              {...(isExternal
                ? { target: "_blank", rel: "noopener noreferrer" }
                : {})}
              className="group flex h-10 w-10 items-center justify-center rounded-full border border-border bg-card/60 text-muted-foreground transition-all duration-300 hover:-translate-y-1 hover:border-primary/50 hover:text-primary"
            >
              <Icon className="h-[18px] w-[18px]" />
            </a>
          </li>
        );
      })}
    </ul>
  );
}
