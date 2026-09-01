kandas/
========

LaTeX source for the **Taittiriya Samhita** of the Krishna Yajurveda. This is
the source used by `SamhitaBook-*.tex` at the repo root — see the root
[README](../README.md) for how the books and format variants fit together.

- **`TaittiriyaSamhita-Kandas.tex`** — the full text: all seven Kandas
  (books) of the Taittiriya Samhita, each divided into Prapathakas and
  Anuvakas. This is the file `\input` by `SamhitaBook-*.tex`, and is the
  actual source of truth for this content.
- **`TaittiriyaSamhita-Kandam-N.tex`** (N = 1–7) — the same content split
  one file per Kanda, for easier standalone reading/reference.
- **`TaittiriyaSamhita-N-M.tex`** (e.g. `1-1` … `7-5`) — the same content
  split further, one file per Kanda+Prapathaka.
- **`TaittiriyaSamhita-Kandas.orig.tex`** / **`.R0.tex`** — earlier snapshots
  of the master file, kept for reference/comparison.
- **`splitPrashnas.sh`** — the maintenance script that produces the
  `Kandam-N` and `N-M` splits from the master file.
- **`clean_text.py`** — a copy of the root `cleanText.py` text-cleanup
  utility, kept local to this folder for convenience.

Pre-rendered, single-section PDFs live in the sibling `kandas-kindle-pdf/`
and `kandas-kindle-scribe-pdf/` folders (there is currently no plain
`kandas-pdf/`) — see the root README's format table for what each suffix
means.

---

*The README.md files on this repo were generated and beautified with Claude.*
