---
name: scfm-evidence-explorer
description: Use when asked to build, rebuild or open the Evidence Explorer from scfm-evidence-review CSVs, or after an scfm-evidence-review run when the reader wants an easier way to look through the scores. Turns every CSV given into one self-contained, offline HTML page.
---

# scFM Evidence Explorer

The CSVs written by the `scfm-evidence-review` skill are the record. A reader usually wants something easier to look through, so offer to build the **Evidence Explorer**: one self-contained HTML page with two views.
- **By task:** the reader picks a task family ("I want a model for genetic perturbation"). Each model evaluated on it shows its per-task checks, then the whole-model checks. Clicking any score opens the question, the reason and the paper's own words.
- **Badge:** models whose `knowledge_source` includes `text` carry a "Text-derived inputs" badge, explained in the model card.
- **Compare models:** every scored model side by side. One table shows what each model was evaluated on (count of evaluations per task family). The other shows the checks: counts of 2/1/0 for the per-task columns, never an average; one score each for the whole-model columns; run-to-run spread; any contradicted claim.

## Build it

Run the script next to this file (standard-library Python, no internet needed). Use the full path to this skill's folder:
```
python3 <this skill's folder>/build_explorer.py <folder>/*.csv --out evidence_explorer.html
```
Give it every CSV the reader has scored, not only today's: the page always shows all models it is given, and if a model appears in several runs it keeps the newest run. Add `--note "Private draft"` to print a line under the title. The template, `explorer_template.html`, must stay next to the script. If either file is missing, say so and offer the CSV and the summary instead; don't hand-build a different page.

## What the reader can keep

The page is a file. Open it in any browser, offline, as often as they like; save it, email it. It holds its own data, so nothing needs regenerating to look at it again. Rebuild only after scoring another model, by rerunning the same command over the folder. Buttons on the page: **Download scores (CSV)** saves the scores it contains, and **Print or save as PDF** prints the current view (landscape). A link ending in `#compare` or `#<task family>` opens that view directly.

Before anyone shares the page, remind them that it shows the reviewer's reading of other groups' papers. Describe it accurately and attribute charitably: the scores record what a paper reported, not whether its results are right.
