#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the 6 MTBB sales pages from 2 templates + content.py.

Usage:  python3 build/generate.py

Reads:
  build/template-preco.html
  build/template-lista.html
  build/content.py   (the PAGES dict)

Writes (overwrites) at repo root:
  publicado.html, escrevendo.html, lancando.html,
  publicado-lista.html, escrevendo-lista.html, lancando-lista.html

This script is self-contained: it does NOT read the original 6 HTML files.
It errors loudly if any {{TOKEN}} is left unsubstituted, or if a content
token has no matching placeholder in the template.
"""
import os
import io
import re
import sys

BUILD_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BUILD_DIR)

# import PAGES from content.py living next to this script
sys.path.insert(0, BUILD_DIR)
from content import PAGES  # noqa: E402

TEMPLATE_FILE = {
    "preco": os.path.join(BUILD_DIR, "template-preco.html"),
    "lista": os.path.join(BUILD_DIR, "template-lista.html"),
}

TOKEN_RE = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


def read(path):
    with io.open(path, "r", encoding="utf-8", newline="") as f:
        return f.read()


def write(path, text):
    with io.open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def render(slug, page):
    variant = page.get("variant")
    if variant not in TEMPLATE_FILE:
        raise SystemExit("ERROR [%s]: unknown variant %r" % (slug, variant))
    template = read(TEMPLATE_FILE[variant])

    # placeholders present in the template
    tpl_tokens = set(TOKEN_RE.findall(template))

    # tokens provided by content (everything except the meta key "variant")
    content_tokens = {k: v for k, v in page.items() if k != "variant"}

    # every content token must correspond to a placeholder
    extra = set(content_tokens) - tpl_tokens
    if extra:
        raise SystemExit(
            "ERROR [%s]: content has token(s) with no placeholder in template-%s.html: %s"
            % (slug, variant, ", ".join(sorted(extra)))
        )
    # every placeholder must be supplied by content
    missing = tpl_tokens - set(content_tokens)
    if missing:
        raise SystemExit(
            "ERROR [%s]: template-%s.html has placeholder(s) with no content value: %s"
            % (slug, variant, ", ".join(sorted(missing)))
        )

    out = template
    for token, value in content_tokens.items():
        out = out.replace("{{%s}}" % token, value)

    # nothing left unsubstituted
    leftover = TOKEN_RE.findall(out)
    if leftover:
        raise SystemExit(
            "ERROR [%s]: unsubstituted placeholder(s) remain: %s"
            % (slug, ", ".join(sorted(set(leftover))))
        )
    return out


def main():
    count = 0
    for slug, page in PAGES.items():
        html = render(slug, page)
        write(os.path.join(ROOT, slug + ".html"), html)
        count += 1
        print("generated %s.html" % slug)
    print("done: %d pages" % count)


if __name__ == "__main__":
    main()
