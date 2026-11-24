# Audit data: 14 single-cell foundation models (rubric v1.7)

Scores from reviewing 14 published model papers with the `scfm-evidence-review` skill, rubric v1.7. Browse them in the Evidence Explorer: https://leahmatzat.github.io/scfm-evidence-review/

| File | What it is |
|---|---|
| `final_scores_v1.7.csv` | All 14 models, one row per fact, score or flag (the skill's fixed CSV format) |
| `models/<Model>_final_v1.7.csv` | The same rows, one file per model |
| `CHANGES_v1.7.md` | What the v1.7 recheck changed (wording, corpus-match evidence, register notes; no score changes) |

Models: CellFM, CellOT, CellPLM, CPA, GEARS, Geneformer, scFoundation, scGPT, SCimilarity, STATE, UCE, X-Cell (the twelve the rubric was developed on), and TranscriptFormer and Scouter (two papers it was tested on afterwards).

## How it was made
Each paper was first scored blind by Claude with the skill, then checked against the sources: every score carries a pointer (version · section or figure · short quote). Review notes inside a value (`[Review …]`, `[Recheck …]`) and the `flags` column record what changed after the blind run and why. `[V]` marks anything that could not be verified.

## What it is not
A score records whether a paper reported a check, not whether its results are right, and not how good the model is. Read each value before relying on a number.

## Licence
CC BY 4.0 (`LICENSE-DATA` in the repository root). Cite the repository's Zenodo DOI: 10.5281/zenodo.23998812.

## Corrections
Open the score in the explorer and use *Suggest a correction*, or open an issue with the correction form.
