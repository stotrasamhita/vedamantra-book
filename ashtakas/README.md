ashtakas/
==========

LaTeX source for the **Taittiriya Brahmana** of the Krishna Yajurveda. This
is the source used by `BrahmanamBook-*.tex` at the repo root — see the root
[README](../README.md) for how the books and format variants fit together.

- **`TaittiriyaBrahmanam-Ashtakams.tex`** — the full text: all eight
  Ashtakas (books) of the Taittiriya Brahmana, each divided into its
  Prapathakas/Prashnas and Anuvakas, in one file. This is the file `\input`
  by `brahmanas.tex` at the repo root, and is the actual source of truth for
  this content.
- **`Achchhidrashvamedha.tex`** — the Ashvamedha-related portion (Ashtaka 3,
  Prashnas 7–9) extracted out for separate reference/reading.
- **`splitPrashnas.sh`** — a maintenance script that splits the monolithic
  `TaittiriyaBrahmanam-Ashtakams.tex` into one file per Ashtaka
  (`TaittiriyaBrahmanam-Ashtakam-N.tex`) and one file per Ashtaka+Prashna
  (`TaittiriyaBrahmanam-N-M.tex`). These generated split files are not
  committed (see the repo `.gitignore`) — they're a scratch aid for
  proofreading/diffing individual sections, not part of the build.

Pre-rendered, single-section PDFs live in the sibling `ashtakas-pdf/`,
`ashtakas-kindle-pdf/`, and `ashtakas-kindle-scribe-pdf/` folders — see the
root README's format table for what each suffix means.

---

*The README.md files on this repo were generated and beautified with Claude.*
