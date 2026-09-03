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
- Chapter 107: `107.디스코스 티스 티키스 (2).txt` — selected and establishes current endpoint.

## Import rule

The canonical selection above means only "used as evidence for this canon import." It does **not** delete or rewrite the author's source archive.

Where selected manuscripts contradict each other internally, the import follows harness policy:

1. do not silently choose a preferred historical/date fact;
2. record the contradiction as an open Finding;
3. keep the affected timeline row marked `CONFLICT` until author resolution;
4. do not propagate the conflicting date into higher-level canon as settled fact.

## Open import issues

- Missing filename/chapter number 69.
- Chapter 26 → 31 date/elapsed-time contradiction.
- Chapters 36–37 → 40 chronological rollback contradiction.
- Chapter 92 contains `1991년 1월` for Manuel's birth, contextually an obvious typo for 1191.
- `메가스 심볼로스` / `메가스 심불로스` spelling oscillates.
- Yusuf's nisba/name spelling oscillates (`알라다키` / `알라디키`).

See `reviews/open/IMPORT-*.json`.
