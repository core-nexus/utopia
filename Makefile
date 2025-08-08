.PHONY: all clean docs-html docs-pdf slides-html slides-pdf validate-storyboard

all: docs-html slides-html

docs-html:
	@bash scripts/render_docs.sh || true

docs-pdf:
	@PANDOC_EXISTS=$$(command -v pandoc >/dev/null 2>&1 && echo yes || echo no); \
	if [ "$$PANDOC_EXISTS" = "yes" ]; then \
		pandoc docs/report.md -s -o docs/report.pdf; \
	else \
		echo "pandoc not found; use CI"; \
	fi

slides-html:
	@bash scripts/render_slides.sh || true

slides-pdf:
	@MARP_EXISTS=$$(command -v marp >/dev/null 2>&1 && echo yes || echo no); \
	if [ "$$MARP_EXISTS" = "yes" ]; then \
		marp --pdf --allow-local-files --output slides/talk.pdf slides/talk.md; \
	else \
		echo "marp not found; use CI"; \
	fi

validate-storyboard:
	@echo "Validate storyboard.json against schema (requires ajv-cli)"
	@echo "Example: npx ajv validate -s schemas/storyboard.schema.json -d video/storyboard.json"

clean:
	rm -f docs/report.html docs/report.pdf slides/talk.html slides/talk.pdf
