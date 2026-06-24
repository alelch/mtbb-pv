#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ONE-OFF bootstrap script. NOT used by the runtime generator.

Reads the 6 real HTML files, slices each per-stage-varying region out using
stable ANCHOR substrings, then:
  1. writes build/template-preco.html   (from publicado.html)
  2. writes build/template-lista.html   (from publicado-lista.html)
  3. writes build/content.py            (the PAGES dict)

Slot value = text strictly BETWEEN a start-anchor and an end-anchor.
The anchors themselves stay in the template (they are shared across stages).

Run:  python3 build/_extract.py
"""
import os
import io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(name):
    with io.open(os.path.join(ROOT, name), "r", encoding="utf-8", newline="") as f:
        return f.read()


# ---------------------------------------------------------------------------
# Anchor definitions.
#   Each token => (start_anchor, end_anchor)
#   The value is everything strictly between the FIRST occurrence of start_anchor
#   (after its end) and the next occurrence of end_anchor.
# Anchors must be byte-identical & uniquely positioned across all stages.
# ---------------------------------------------------------------------------

# Shared between preco and lista (same structural anchors).
COMMON_ANCHORS = {
    # Whole SEO head region between viewport and og:site_name.
    "SEO_HEAD": (
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n',
        '\n<meta property="og:site_name" content="Método The Book Business">',
    ),
    # The application/ld+json one-liner (full <script> line content).
    "LDJSON": (
        '<script type="application/ld+json">',
        "</script>",
    ),
    # Hero badge + h1 (block).
    "HERO_BADGE_H1": (
        '    <div class="hero-logo"><img src="assets/logo-metodo-the-book-business.webp" alt="Método The Book Business" width="111" height="60" fetchpriority="high"></div>\n',
        '\n    <p class="hero-sub">',
    ),
    # Hero watch line text (inside the <p class="hero-watch"> ... </p>).
    "HERO_WATCH": (
        '    <p class="hero-watch">',
        "</p>\n  </div>\n</section>",
    ),
    # Journey section title text (anchored on the unique journey eyebrow).
    "JOURNEY_TITLE": (
        '<p class="section-eyebrow">A transformação completa</p>\n    <h2 class="section-title">',
        "</h2>\n    <p class=\"section-subtitle\">Cada etapa existe por uma razão.",
    ),
    # Journey steps inner block.
    "JOURNEY_STEPS": (
        '    <div class="journey-steps">\n',
        '\n    </div>\n    <p style="text-align:center; margin-top:48px;',
    ),
    # pc-text h2.
    "PC_TEXT": (
        '    <h2 class="pc-text">',
        '</h2>\n    <a href="#" class="btn-cta btn-cta--dark large open-modal"',
    ),
    # Mentoria line ("Você valida cada decisão...").
    "MENTORIA": (
        "          <h3>Encontros ao Vivo com a Dany</h3>\n          <p>",
        '</p>\n          <p class="live-cta">',
    ),
    # FAQ list inner (the <details> items).
    "FAQ_LIST": (
        '    <div class="faq-list">\n',
        "\n    </div>\n  </div>\n</section>\n\n<!-- BLOCO 17 — CTA FINAL -->",
    ),
}

# AGITATION_BLOCK proper anchors (the CTA-pós-vídeo close differs preco vs lista
# only in the trailing markup AFTER agitation, so we anchor on shared comments).
AGITATION_START = (
    '<!-- CTA PÓS-VÍDEO -->\n<div style="text-align: center; padding: 0 24px 56px;">\n'
    '  <p style="font-size:clamp(15px,1.8vw,18px); color:var(--text-soft); margin:0 auto 14px; max-width:520px; line-height:1.7;">'
)
# We split the CTA-pós-vídeo line into its own token, then the agitation block
# starts right after the CTA-pós-vídeo closing </div>.

# Per-variant extra/override anchors.
PRECO_ANCHORS = dict(COMMON_ANCHORS)
LISTA_ANCHORS = dict(COMMON_ANCHORS)

# CTA pós-vídeo line text (the <p> just below the video).
CTA_POSVIDEO = (
    '  <p style="font-size:clamp(15px,1.8vw,18px); color:var(--text-soft); margin:0 auto 14px; max-width:520px; line-height:1.7;">',
    "</p>\n  <a href=\"#\" class=\"btn-cta large open-modal\"",
)

# Agitation block: between the CTA-pós-vídeo block close and BLOCO 6 JORNADA.
# The CTA-pós-vídeo block ends differently per variant (trust div vs waitlist note),
# so the START anchor is variant-specific. The captured value includes lancando's
# structural <!-- BLOCO 3 — NÚMEROS --> comment variance + the TESE pull-quote.
AGITATION_END = "<!-- BLOCO 6 — JORNADA -->"
AGITATION_START = {
    "preco": "</svg>Compra segura</span></div>\n</div>\n",
    "lista": "🔒 Vagas limitadas · Você é avisado primeiro</p>\n</div>\n",
}

# Garantia/offer closing markup just before BLOCO 12 — BIO DANY.
# lancando.html carries an extra stray closing wrapper here (pre-existing in the
# live file), so the closing markup varies by stage. Captured as a whole block.
# START anchor is variant-specific (different garantia block per variant); END is shared.
GARANTIA_CLOSE_END = "<!-- BLOCO 12 — BIO DANY -->"
GARANTIA_CLOSE_START = {
    "preco": '            <span class="gv9-sign-rule"></span>\n',
    "lista": '      <p style="font-size: 12px; color: rgba(255,255,255,0.4); margin-top: 16px;">Sem compromisso · Você pode sair a qualquer momento</p>\n',
}

# Final CTA h2 + p (the <h2>...</h2>\n    <p ...>...</p>).
FINAL_CTA = (
    '<!-- BLOCO 17 — CTA FINAL -->\n<section class="final-cta">\n  <div class="container">\n    ',
    '\n    <a href="#" class="btn-cta large open-modal"',
)

# Inline JS stage slug — appears literally twice as  stage: 'SLUG'
# We don't anchor-extract this; it equals the page slug minus "-lista".


def slice_between(text, start, end, label):
    i = text.find(start)
    if i < 0:
        raise SystemExit("EXTRACT ERROR [%s]: start anchor not found" % label)
    if text.find(start, i + len(start)) >= 0:
        raise SystemExit("EXTRACT ERROR [%s]: start anchor not unique" % label)
    vstart = i + len(start)
    j = text.find(end, vstart)
    if j < 0:
        raise SystemExit("EXTRACT ERROR [%s]: end anchor not found after start" % label)
    return text[vstart:j], vstart, j


# Token -> (start, end) anchor map (final, clean). Variant-specific where needed.
def anchor_map(variant):
    return {
        "SEO_HEAD": COMMON_ANCHORS["SEO_HEAD"],
        "LDJSON": COMMON_ANCHORS["LDJSON"],
        "HERO_BADGE_H1": COMMON_ANCHORS["HERO_BADGE_H1"],
        "HERO_WATCH": COMMON_ANCHORS["HERO_WATCH"],
        "CTA_POSVIDEO": CTA_POSVIDEO,
        "AGITATION_BLOCK": (AGITATION_START[variant], AGITATION_END),
        "JOURNEY_TITLE": COMMON_ANCHORS["JOURNEY_TITLE"],
        "JOURNEY_STEPS": COMMON_ANCHORS["JOURNEY_STEPS"],
        "PC_TEXT": COMMON_ANCHORS["PC_TEXT"],
        "MENTORIA": COMMON_ANCHORS["MENTORIA"],
        "GARANTIA_CLOSE": (GARANTIA_CLOSE_START[variant], GARANTIA_CLOSE_END),
        "FAQ_LIST": COMMON_ANCHORS["FAQ_LIST"],
        "FINAL_CTA": FINAL_CTA,
    }


# Order matters when building the template: process by position so offsets stay valid.
TOKEN_ORDER = [
    "SEO_HEAD", "LDJSON", "HERO_BADGE_H1", "HERO_WATCH", "CTA_POSVIDEO",
    "AGITATION_BLOCK", "JOURNEY_TITLE", "JOURNEY_STEPS", "PC_TEXT",
    "MENTORIA", "GARANTIA_CLOSE", "FAQ_LIST", "FINAL_CTA",
]

PAGES = {
    "publicado": ("preco", "publicado.html"),
    "escrevendo": ("preco", "escrevendo.html"),
    "lancando": ("preco", "lancando.html"),
    "publicado-lista": ("lista", "publicado-lista.html"),
    "escrevendo-lista": ("lista", "escrevendo-lista.html"),
    "lancando-lista": ("lista", "lancando-lista.html"),
}

GOLDEN = {"preco": "publicado.html", "lista": "publicado-lista.html"}


def build_template(golden_text, variant):
    amap = anchor_map(variant)
    # collect (vstart, vend, token) by scanning
    spans = []
    for tok in TOKEN_ORDER:
        start, end = amap[tok]
        _, vs, ve = slice_between(golden_text, start, end, tok)
        spans.append((vs, ve, tok))
    spans.sort()
    # ensure no overlap
    for k in range(1, len(spans)):
        if spans[k][0] < spans[k - 1][1]:
            raise SystemExit("EXTRACT ERROR: overlapping spans %s / %s" % (spans[k - 1][2], spans[k][2]))
    out = []
    cursor = 0
    for vs, ve, tok in spans:
        out.append(golden_text[cursor:vs])
        out.append("{{%s}}" % tok)
        cursor = ve
    out.append(golden_text[cursor:])
    tpl = "".join(out)
    # Now handle the STAGE_SLUG token: replace the two JS occurrences.
    # Golden slug for preco = 'publicado', lista = 'publicado-lista'.
    return tpl


def extract_tokens(text, slug, variant):
    amap = anchor_map(variant)
    vals = {}
    for tok in TOKEN_ORDER:
        start, end = amap[tok]
        v, _, _ = slice_between(text, start, end, tok + " @" + slug)
        vals[tok] = v
    return vals


def py_repr(s):
    # Use triple-quoted string. Escape backslashes and triple quotes minimally.
    if '"""' not in s and not s.endswith('"'):
        # Prefer raw-ish triple-quote; but backslashes in JS (\D, \d) must survive.
        # Triple-quoted normal string would interpret \D as \D (unknown escape kept) but
        # to be 100% safe we escape backslashes.
        pass
    body = s.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
    return '"""' + body + '"""'


def main():
    # Build templates from golden files.
    for variant, gname in GOLDEN.items():
        gtext = read(gname)
        tpl = build_template(gtext, variant)
        # STAGE_SLUG: replace both JS stage occurrences in the template.
        # The JS stage value is the BASE stage (no -lista suffix) for BOTH variants.
        gslug = "publicado"
        tpl2 = tpl.replace("stage: '%s'," % gslug, "stage: '{{STAGE_SLUG}}',")
        n = tpl.count("stage: '%s'," % gslug)
        if n != 2:
            raise SystemExit("EXTRACT ERROR: expected 2 stage occurrences in %s, found %d" % (gname, n))
        with io.open(os.path.join(ROOT, "build", "template-%s.html" % variant),
                     "w", encoding="utf-8", newline="") as f:
            f.write(tpl2)
        print("wrote build/template-%s.html (%d tokens, %d {{}} placeholders)"
              % (variant, len(TOKEN_ORDER) + 1, tpl2.count("{{")))

    # Build content.py
    lines = []
    lines.append("# -*- coding: utf-8 -*-")
    lines.append('"""')
    lines.append("Per-page content for the 6 MTBB sales pages.")
    lines.append("Edit copy HERE, then run:  python3 build/generate.py")
    lines.append("")
    lines.append("Each page maps slug -> dict of token values.")
    lines.append('\"variant\" picks the template (template-preco.html / template-lista.html).')
    lines.append("HTML-fragment tokens use triple-quoted strings.")
    lines.append('"""')
    lines.append("")
    lines.append("PAGES = {")
    for slug, (variant, fname) in PAGES.items():
        text = read(fname)
        toks = extract_tokens(text, slug, variant)
        # the JS stage value is the base stage (strip the -lista suffix)
        stage_slug = slug[:-6] if slug.endswith("-lista") else slug
        lines.append("    %r: {" % slug)
        lines.append('        "variant": %r,' % variant)
        lines.append('        "STAGE_SLUG": %r,' % stage_slug)
        for tok in TOKEN_ORDER:
            lines.append('        "%s": %s,' % (tok, py_repr(toks[tok])))
        lines.append("    },")
    lines.append("}")
    lines.append("")
    with io.open(os.path.join(ROOT, "build", "content.py"), "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(lines))
    print("wrote build/content.py (%d pages)" % len(PAGES))


if __name__ == "__main__":
    main()
