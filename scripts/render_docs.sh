#!/usr/bin/env bash
set -euo pipefail

in="docs/report.md"
out_html="docs/report.html"
out_pdf="docs/report.pdf"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "pandoc not found. Install pandoc or use CI."
  exit 1
fi

echo "Rendering $in → $out_html"
pandoc "$in" -s -o "$out_html"

if command -v wkhtmltopdf >/dev/null 2>&1; then
  echo "Rendering $in → $out_pdf (wkhtmltopdf engine)"
  pandoc "$in" -s --pdf-engine=wkhtmltopdf -o "$out_pdf"
else
  echo "Skipping PDF (LaTeX or wkhtmltopdf not found)."
fi
