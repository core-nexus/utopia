#!/usr/bin/env bash
set -euo pipefail

in="slides/talk.md"
out_html="slides/talk.html"
out_pdf="slides/talk.pdf"

if ! command -v marp >/dev/null 2>&1; then
  echo "marp (marp-cli) not found. Install via npm or use CI."
  exit 1
fi

echo "Rendering $in → $out_html"
marp --html --allow-local-files --output "$out_html" "$in"

echo "Rendering $in → $out_pdf"
marp --pdf --allow-local-files --output "$out_pdf" "$in"
