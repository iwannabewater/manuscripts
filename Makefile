.PHONY: fonts test verify verify-network render-pdfs

PYTHON ?= .venv/bin/python

fonts:
	./scripts/ensure_fonts.sh

test: verify

verify: fonts
	node scripts/verify_repo.mjs

verify-network:
	node scripts/verify_sources_network.mjs

render-pdfs: fonts
	$(PYTHON) scripts/render_pdfs.py
