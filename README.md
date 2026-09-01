vedamantra-book
================

A LaTeX (XeLaTeX) source collection of Vedic texts in Devanagari, built into
several ready-to-read PDF books. The content is drawn from the **Taittiriya
Shakha of the Krishna Yajurveda** — its Samhita, Brahmana, and Aranyaka (with
the Taittiriya and Mahanarayana Upanishads) — plus a separate collection of
commonly recited mantras and suktas used in daily worship.

This repository's top level is intentionally dense: every book exists as
several pre-rendered PDFs, one per reading device/format. This README exists
mainly to explain that scheme so you're not lost among the files.

For personal study use; not for commercial printing or distribution. See
also <http://stotrasamhita.github.io/about/>.

## The four books

| Book (root file prefix) | Content | Source folder | Read it |
|---|---|---|---|
| `vedamantrabook` | **Mantras** — a standalone collection of suktas, nyasas and mantras commonly used in daily worship (Purusha Suktam, Sri Suktam, Rudra Prashna/Chamakam, Mantra Pushpam, Sandhyavandanam, etc.) | `mantras/` | [`vedamantrabook.pdf`](https://github.com/stotrasamhita/vedamantra-book/blob/master/vedamantrabook.pdf) |
| `AraNyakabook` | **Aranyakam** — the Taittiriya Aranyaka (its ten Prashnas, including the Taittiriya and Mahanarayana Upanishads) plus the Kathaka portion | `aranyakas/` | [`AraNyakabook-print.pdf`](https://github.com/stotrasamhita/vedamantra-book/blob/master/AraNyakabook-print.pdf) |
| `BrahmanamBook` | **Brahmanam** — the Taittiriya Brahmana (all eight Ashtakas), with the Aranyaka appended at the end | `ashtakas/` (+ `aranyakas/`) | [`BrahmanamBook-print.pdf`](https://github.com/stotrasamhita/vedamantra-book/blob/master/BrahmanamBook-print.pdf) |
| `SamhitaBook` | **Samhita** — the Taittiriya Samhita (all seven Kandas) | `kandas/` | [`SamhitaBook-kindle.pdf`](https://github.com/stotrasamhita/vedamantra-book/blob/master/SamhitaBook-kindle.pdf) (no `-print` edition exists yet — see the format table below) |

Each book's master `.tex` file at the root (e.g. `AraNyakabook-print.tex`)
`\input`s the corresponding folder's content; the folder itself holds the
real source text, split one file per section. `vedamantrabook.tex` (no
suffix) is the default/base build of the mantra book; `mantras.tex`,
`aranyakas.tex`, and `brahmanas.tex` at the root are the "content assembly"
files each book's variants share.

## The format suffixes

Every book is typeset multiple times, once per target device/format, because
margins, page size, and font size all need to change to suit the reader:

| Suffix | Format | Page size | Notes |
|---|---|---|---|
| *(none)* | Default/digital | 148×210mm (A5-ish) | Base portrait layout, screen or tablet reading |
| `-kindle` | Kindle e-reader | 126×168mm | Small trim, tight margins |
| `-kindle-scribe` | Kindle Scribe | 140×185mm | Larger e-ink tablet |
| `-kindle-lscape` | Kindle, landscape | 126×168mm, landscape | Same Kindle trim, rotated — wider line length |
| `-print` | Physical printing | 148×210mm | Adds binding-aware inner/outer margins (odd/even side offsets) |
| `-rM` | reMarkable tablet | 6.18×8.24in | Sized to the reMarkable's screen |

Not every book has every variant — only the combinations that were actually
produced exist (e.g. `SamhitaBook` currently has `-kindle` and
`-kindle-scribe` only; `-rM` currently only exists for `BrahmanamBook`).

Each `<name>.tex` has a same-named `.pdf` sitting next to it — that PDF is
the pre-built output of that `.tex` file, checked in for convenience so you
don't need a LaTeX toolchain just to read the book.

> **Note:** `BrahmanamBook-kindle - Copy.pdf` and `SamhitaBook-kindle - Copy.pdf`
> at the root appear to be accidental duplicate copies of
> `BrahmanamBook-kindle.pdf` and `SamhitaBook-kindle.pdf` respectively (stray
> " - Copy" suffix from a file manager), not a distinct format. Flagging
> here rather than removing them.

## Folder layout

Each text category has one **source** folder (bare name) plus one sibling
folder per pre-rendered format:

```
aranyakas/                     LaTeX source, one file per Prashna
aranyakas-pdf/                 pre-rendered PDFs, default/digital layout
aranyakas-kindle-pdf/          pre-rendered PDFs, Kindle layout
aranyakas-kindle-scribe-pdf/   pre-rendered PDFs, Kindle Scribe layout
```

...and the same pattern for `ashtakas/`, `kandas/`, and `mantras/`. The
`-pdf` / `-kindle-pdf` / `-kindle-scribe-pdf` folders are mechanical,
per-section mirrors of the source folder (one small standalone PDF per
`.tex` file, useful for reading or sharing a single hymn/section without the
whole book) — see the format table above for what each suffix means. They're
built by a `tex2pdf.sh` script that lives in each `-pdf` folder. Not every
category has every `-pdf` variant (there's no plain `kandas-pdf/`, for
instance — only the two Kindle variants exist for that category).

The source folders have their own README with a description of their
contents:

- [`aranyakas/README.md`](aranyakas/README.md) — the Taittiriya Aranyaka
- [`ashtakas/README.md`](ashtakas/README.md) — the Taittiriya Brahmana
- [`kandas/README.md`](kandas/README.md) — the Taittiriya Samhita
- [`mantras/README.md`](mantras/README.md) — daily-worship mantras and suktas

## Building from source

The books are typeset with **XeLaTeX** (required for the Devanagari/Unicode
handling and OpenType font features used throughout). You'll need:

- A TeX distribution with `xelatex` (e.g. TeX Live).
- The **Siddhanta** font (Devanagari) installed and available to `fontspec`.
- Standard LaTeX packages used by `preamble.tex`: `etoolbox`, `fancyhdr`,
  `hyperref`, plus the project's own `shloka.sty` and `mantra.sty` style
  files (in this repo already).

To build one variant of one book, run `xelatex` on its root `.tex` file
twice (once to generate the table of contents/bookmarks, once to resolve
them), e.g.:

```sh
xelatex AraNyakabook-print.tex
xelatex AraNyakabook-print.tex
```

Each `-pdf` sibling folder (e.g. `aranyakas-pdf/`) has a `tex2pdf.sh` that
rebuilds per-section PDFs from the corresponding source folder, skipping
files whose PDF is already newer than the source.

A few small Python utilities assist with text maintenance (not part of the
build itself):

- `cleanText.py` — applies a fixed set of Vedic-accent/consonant-cluster
  text substitutions (e.g. normalizing anusvara-before-sibilant spellings)
  across the given files, and flags words where automatic ITRANS
  transliteration suggests a further fix may be needed.
- `performSiddhantaFontFixes.py` / `revertSiddhantaFontFixes.py` — apply or
  undo a couple of ligature substitutions (`ष्ट्य`→`ट्य`, `ष्ठ्य`→`ठ्य`)
  needed to work around rendering quirks of the Siddhanta font.

## Colophon

Typeset with XeLaTeX using the Siddhanta font and LaTeX macros by
H. L. Prasād; the great majority of the Devanagari encoding was done with
Ajit Krishnan's Mudgala IME. Initial ITRANS encodings of some texts came
from sanskritdocuments.org and sa.wikisource.org; the Kathaka text is based
on an edition by Subramania Sarma, shared via Ulrich Stiehl's
sanskritweb.de.

For personal use only — not for commercial printing or distribution.

---

*The README.md files on this repo were generated and beautified with Claude.*
