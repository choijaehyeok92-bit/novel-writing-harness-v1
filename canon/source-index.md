# Manuscript Import Manifest — 2026-09-04

## Source

- Uploaded archive: `3년 뒤 살해당하는 동로마 황제가 되었다.zip`
- Text files found: **109**
- Encoding: UTF-8/UTF-8-SIG text manuscripts.
- Imported purpose: derive canon only. The manuscript files themselves were **not** uploaded into this repository by this operation.

## Canonical chapter selection for this import

- Normal sequence accepted as source: chapters **1–68**, **70–95**, **97–105**, **107**.
- Chapter **69** is absent from the archive. This import does **not** renumber later chapters.
- Chapter 96 has three source files:
  - `96.내부정리.txt` — superseded for this import.
  - `96.반석.txt` — superseded for this import.
  - `96.반석닦기.txt` — **selected**, latest archive revision and ~98% similar to immediately prior revision.
- Chapter 106 has two source files:
  - `106.디스코스 티스 타키스.txt` — superseded for this import.
  - `106.디스코스 티스 티키스.txt` — **selected**, latest archive revision and ~98% similar to prior revision.
- Chapter 107: `107.디스코스 티스 티키스 (2).txt` — selected and established the archive-import endpoint.

## Post-import reviewed canonical additions

The following later manuscripts are **reviewed and author-approved canonical sources** stored under `manuscripts/reviewed/`:

- Chapter 108: `manuscripts/reviewed/108.바실리케 켈리티카.txt`
- Chapter 109: `manuscripts/reviewed/109.한 시대가 저물고.txt`
- Chapter 110: `manuscripts/reviewed/110.하인리히.txt`
- Chapter 111: `manuscripts/reviewed/111.미래를 그리다.txt`
- Chapter 112: `manuscripts/reviewed/112.폴레미키 스홀리.txt`
- Chapter 113: `manuscripts/reviewed/113.시칠리아.txt`
- Chapter 114: `manuscripts/reviewed/114.시칠리아 (2).txt`
- Chapter 115: `manuscripts/reviewed/115.산통.txt`
- Chapter 116: `manuscripts/reviewed/116.양 로마 대전.txt`
- Chapter 117: `manuscripts/reviewed/117.양 로마 대전 (2).txt`
- Chapter 118: `manuscripts/reviewed/118.성 마르코 공황.txt`

**Current canonical manuscript endpoint: Chapter 118, `성 마르코 공황`.**

Chapter-specific canon extraction and later override/addendum files under `canon/` supersede stale endpoint statements in older high-level canon documents while preserving the original import record.

## Import rule

The canonical selection above means only "used as evidence for this canon import." It does **not** delete or rewrite the author's source archive.

Where selected manuscripts contradict each other internally, the import follows harness policy:

1. do not silently choose a preferred historical/date fact;
2. record the contradiction as an open Finding;
3. keep the affected timeline row marked `CONFLICT` until author resolution;
4. do not propagate the conflicting date into higher-level canon as settled fact.

Reviewed post-import chapters are added as later canonical sources without retroactively changing the archive-selection record above.

## Open import issues

- Missing filename/chapter number 69.
- Chapter 26 → 31 date/elapsed-time contradiction.
- Chapters 36–37 → 40 chronological rollback contradiction.
- Chapter 92 contains `1991년 1월` for Manuel's birth, contextually an obvious typo for 1191.
- `메가스 심볼로스` / `메가스 심불로스` spelling oscillates.
- Yusuf's nisba/name spelling oscillates (`알라다키` / `알라디키`).

See `reviews/open/IMPORT-*.json`.
