# scFM Evidence Review

Review the evidence in a single-cell foundation model paper the same way every time. Give Claude a paper (and its supplements), and the skill records which standard checks the paper reported, task by task, each backed by a pointer and a short quote from the paper.

It measures **what was reported**, using a fixed rubric (v1.6). It does not rerun models or judge whether results are true.

## What you get

- **One CSV per paper**, in a fixed long format, so reviews of different models stack into one table.
- **Table 1: what the model is.** Facts such as class, architecture, gene coverage, where its knowledge comes from (measured expression, protein sequence, curated knowledge, or text read by a language model), availability of weights and code, what was held out, and run-to-run spread.
- **Table 2: what the paper reported**, scored 2 / 1 / 0 / n/a on nine checks: simple baseline, input dependence, pretraining payoff, unwanted variation, prior dependence, training-data overlap, fair test number, explanation check and biological validation. Four of them are scored per task.
- **Flags:** version differences, claims contradicted by the paper's own data, unverified items, notes and reviewer observations.
- **Evidence Explorer (optional):** one self-contained HTML page that shows every model you have scored, by task and side by side. It opens offline in any browser.

## How to use it

Ask Claude to review a paper, for example: *"Review the evidence in this paper with the scfm-evidence-review skill"*, and attach the article, supplements, source data and peer review file if there is one. Claude reads the rubric, reads the files, writes `<Model>_<date>.csv` and shows a short summary. To build the explorer from all your CSVs:

```
python3 skills/scfm-evidence-review/explorer/build_explorer.py <folder>/*.csv --out evidence_explorer.html
```

Use the strongest model available; smaller models read less of each paper and miss more.

## What it reads, runs and sends

- **Reads** the files you give it, and public web pages: the paper's code repository, model card and data pages (to check availability), and papers that evaluated the model independently.
- **Runs** `build_explorer.py` (Python standard library only) only when you ask for the explorer. It reads your CSVs and writes one HTML file.
- **Writes** files only in your working folder: the CSV, and the explorer page if requested.
- **Sends** nothing anywhere else. The explorer page makes no network requests.

## Licence

MIT. See `LICENSE`.
