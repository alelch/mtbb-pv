const __vite__mapDeps=(i,m=__vite__mapDeps,d=(m.f||(m.f=["./ComparisonSection-DW-I9COq.js","./index-Cz7pRKoM.js","./index-ClVSohdt.css","./TargetSection-CgUlaave.js","./check-V2TZxhaN.js","./EventContentSection-Cy2za70y.js","./ScheduleSection-BT2ZXdgz.js","./SocialProofSection-CkZaA8E0.js","./depo-4-cgfml7rq.js","./depo-robson-CE2n1ArY.js","./play-BmrCCLxp.js","./index-CVfgbIN8.js","./PricingSection-DgIydHzg.js","./zap-CDmGkW_H.js","./shield-check-C6bfE5vS.js","./rotate-ccw-H_l6oTv_.js","./MentorSection-J4j2a0-4.js","./dany-bio-fwK8WGUq.js","./target-C0opr8_Z.js","./GuaranteeSection-Cr9s_rAc.js","./FAQSection-du-ntKlC.js","./message-circle-CePNrtlh.js","./chevron-down-CAWg9yNY.js","./FooterCTA-BZqa6FT7.js","./shield-KGHLkI84.js","./StickyCTA-BVG-_RLy.js"])))=>i.map(i=>d[i]);
import{r as e,_ as o,j as r,p as a,H as t,q as s}from"./index-Cz7pRKoM.js";const n=e.lazy(()=>o(()=>import("./ComparisonSection-DW-I9COq.js"),__vite__mapDeps([0,1,2]),import.meta.url)),i=e.lazy(()=>o(()=>import("./TargetSection-CgUlaave.js"),__vite__mapDeps([3,1,2,4]),import.meta.url)),l=e.lazy(()=>o(()=>import("./EventContentSection-Cy2za70y.js"),__vite__mapDeps([5,1,2]),import.meta.url)),d=e.lazy(()=>o(()=>import("./ScheduleSection-BT2ZXdgz.js"),__vite__mapDeps([6,1,2]),import.meta.url)),p=e.lazy(()=>o(()=>import("./SocialProofSection-CkZaA8E0.js"),__vite__mapDeps([7,1,2,8,9,10,11]),import.meta.url)),c=e.lazy(()=>o(()=>import("./PricingSection-DgIydHzg.js"),__vite__mapDeps([12,1,2,4,13,14,15]),import.meta.url)),h=e.lazy(()=>o(()=>import("./MentorSection-J4j2a0-4.js"),__vite__mapDeps([16,1,2,17,18]),import.meta.url)),m=e.lazy(()=>o(()=>import("./GuaranteeSection-Cr9s_rAc.js"),__vite__mapDeps([19,1,2,14]),import.meta.url)),x=e.lazy(()=>o(()=>import("./FAQSection-du-ntKlC.js"),__vite__mapDeps([20,1,2,21,22]),import.meta.url)),u=e.lazy(()=>o(()=>import("./FooterCTA-BZqa6FT7.js"),__vite__mapDeps([23,1,2,24]),import.meta.url)),g=e.lazy(()=>o(()=>import("./StickyCTA-BVG-_RLy.js"),__vite__mapDeps([25,1,2]),import.meta.url)),b=()=>r.jsxs("div",{className:"v2-theme",children:[r.jsx("style",{children:`
        /* ── V2 LIGHT THEME ────────────────────────────────── */
        .v2-theme {
          --background: 0 0% 100%;
          --foreground: 220 25% 8%;

          --card: 220 20% 97%;
          --card-foreground: 220 25% 8%;

          --popover: 0 0% 100%;
          --popover-foreground: 220 25% 8%;

          /* Verde mais escuro p/ contraste em fundo branco */
          --primary: 78 90% 32%;
          --primary-foreground: 0 0% 100%;

          --secondary: 220 18% 94%;
          --secondary-foreground: 220 25% 8%;

          --muted: 220 15% 92%;
          --muted-foreground: 220 12% 35%;

          --accent: 78 75% 30%;
          --accent-foreground: 0 0% 100%;

          --border: 220 18% 82%;
          --input: 220 15% 88%;
          --ring: 78 90% 32%;

          --gradient-hero: linear-gradient(135deg, hsl(78 90% 32%), hsl(88 75% 26%));
          --gradient-dark: linear-gradient(180deg, hsl(0 0% 100%), hsl(220 18% 96%));
          --gradient-radial: radial-gradient(ellipse at 50% 0%, hsl(78 90% 32% / 0.08) 0%, transparent 60%);
          --shadow-glow: 0 0 40px hsl(78 90% 32% / 0.12), 0 0 80px hsl(78 90% 32% / 0.05);
          --shadow-card: 0 2px 20px hsl(220 25% 8% / 0.07), 0 1px 4px hsl(220 25% 8% / 0.05);
          --shadow-elevated: 0 12px 40px hsl(220 25% 8% / 0.14), 0 2px 8px hsl(220 25% 8% / 0.06);

          background-color: hsl(0 0% 100%);
          color: hsl(220 25% 8%);
        }

        /* ── Grid pattern (fundo claro) */
        .v2-theme .grid-pattern {
          background-image:
            linear-gradient(hsl(220 18% 86%) 1px, transparent 1px),
            linear-gradient(90deg, hsl(220 18% 86%) 1px, transparent 1px);
          background-size: 60px 60px;
        }

        /* ── Divisores */
        .v2-theme .section-glow::before {
          background: linear-gradient(90deg, transparent, hsl(78 90% 32% / 0.18), transparent);
        }

        .v2-theme .divider-gradient {
          background: linear-gradient(90deg, transparent, hsl(78 90% 32% / 0.2), transparent);
        }

        /* ── Botão primário (sombra mais sutil em fundo claro) */
        .v2-theme .btn-primary {
          background-color: hsl(78 90% 32%);
          color: hsl(0 0% 100%);
          box-shadow: 0 4px 20px hsl(78 90% 32% / 0.30), 0 2px 8px hsl(0 0% 0% / 0.12);
        }

        .v2-theme .btn-primary:hover {
          box-shadow: 0 6px 30px hsl(78 90% 32% / 0.40), 0 4px 12px hsl(0 0% 0% / 0.15);
        }

        /* ── Cards com mais definição em fundo branco */
        .v2-theme .card-glass {
          background: hsl(0 0% 100%);
          border: 1px solid hsl(220 18% 86%);
          box-shadow: 0 2px 16px hsl(220 25% 8% / 0.06), 0 1px 3px hsl(220 25% 8% / 0.04);
        }

        .v2-theme .card-highlight {
          background: hsl(0 0% 100%);
          border: 1px solid hsl(78 90% 32% / 0.20);
          box-shadow: 0 0 0 1px hsl(78 90% 32% / 0.08), 0 8px 32px hsl(78 90% 32% / 0.08), 0 2px 8px hsl(220 25% 8% / 0.06);
        }

        /* ── Seções alternadas (bg-secondary/50) mais distintas */
        .v2-theme .noise-overlay {
          position: relative;
        }

        /* Aplica fundo levemente diferente às seções secundárias */
        .v2-theme section.bg-secondary/50 {
          background-color: hsl(220 20% 96%) !important;
        }

        /* ── HeroSection: gradiente lateral vira de branco para transparente */
        .v2-theme [class*="from-background"] {
          --tw-gradient-from: hsl(0 0% 100%);
        }

        /* ── Countdown banner texto legível */
        .v2-theme [class*="bg-primary"] .line-through {
          opacity: 0.65;
        }

        /* ── FAQ cards */
        .v2-theme .border-border/60 {
          border-color: hsl(220 18% 82%);
          background: hsl(0 0% 100%);
        }

        /* ── Social proof card border */
        .v2-theme [style*="0 0 0 1px hsl(var(--border))"] {
          box-shadow: 0 0 0 1px hsl(220 18% 82%), 0 4px 20px hsl(220 25% 8% / 0.10);
        }

        /* ── Texto gradient usa as cores escuras do tema claro */
        .v2-theme .text-gradient {
          background-image: linear-gradient(135deg, hsl(78 90% 28%), hsl(88 75% 22%));
        }

        /* ── Pricing card sombra mais profunda */
        .v2-theme #inscricao .rounded-2xl {
          box-shadow: 0 0 0 1px hsl(78 90% 32% / 0.22),
                      0 8px 40px hsl(78 90% 32% / 0.10),
                      0 24px 60px hsl(220 25% 8% / 0.12) !important;
        }

        /* ── Sticky CTA fundo claro */
        .v2-theme .backdrop-blur-lg {
          background-color: hsl(0 0% 100% / 0.92) !important;
          border-top-color: hsl(220 18% 86%) !important;
        }
      `}),r.jsxs("main",{className:"min-h-screen",style:{backgroundColor:"hsl(0 0% 100%)",color:"hsl(220 20% 10%)"},children:[r.jsx(a,{}),r.jsx(t,{}),r.jsx(s,{}),r.jsxs(e.Suspense,{fallback:null,children:[r.jsx(n,{}),r.jsx(i,{}),r.jsx(l,{}),r.jsx(d,{}),r.jsx(p,{}),r.jsx(c,{}),r.jsx(h,{}),r.jsx(m,{}),r.jsx(x,{}),r.jsx(u,{}),r.jsx(g,{})]})]})]});export{b as default};
