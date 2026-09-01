aranyakas/
===========

LaTeX source for the **Taittiriya Aranyaka** of the Krishna Yajurveda, one
file per Prashna (chapter/reading), plus the Kathaka portion appended at the
end. This is the source used by `AraNyakabook-*.tex` at the repo root (and
reused, with the Brahmana, by `BrahmanamBook-*.tex`) — see the root
[README](../README.md) for how the books and format variants fit together.

| File | Prashna | Contents |
|---|---|---|
| `ArunaPrashnah.tex` | 1 | अरुणप्रश्नः — Aruna Prashna |
| `SahaVai.tex` | 2 | द्वितीयः प्रश्नः |
| `Chittissruk.tex` | 3 | तृतीयः प्रश्नः |
| `NamoVache.tex` | 4 | चतुर्थः प्रश्नः |
| `DevaVai.tex` | 5 | पञ्चमः प्रश्नः |
| `PareyuvaMsam.tex` | 6 | षष्ठः प्रश्नः |
| `Taittiriyopanishat.tex` | 7–9 | शीक्षावल्ली and the rest of the **Taittiriya Upanishad** (Brahmananda Valli, Bhrigu Valli) |
| `Mahanarayanopanishat.tex` | 10 | महानारायणोपनिषत् — the **Mahanarayana Upanishad** |
| `Kathaka.tex` | — | The Kathaka portion appended after the ten Prashnas |

Each file is `\input` in this order by `aranyakas.tex` at the repo root,
which is in turn included by every `AraNyakabook-*` and `BrahmanamBook-*`
variant. The files are meant to be compiled as part of one of those books,
not standalone — each starts with a `% !TeX root = ...` comment pointing at
its parent document.

Pre-rendered, single-section PDFs of this same content live in the sibling
`aranyakas-pdf/`, `aranyakas-kindle-pdf/`, and `aranyakas-kindle-scribe-pdf/`
folders (one small PDF per file above, per format) — see the root README's
format table for what each suffix means.
