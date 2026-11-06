# scfm-evidence-review

A Claude skill for reviewing the evidence in single-cell foundation model papers with a fixed, versioned rubric. For each paper it records which standard checks were reported, task by task, each backed by a pointer and a quote, and writes a CSV that stacks across models. An optional Evidence Explorer turns those CSVs into one offline HTML page.

The rubric (v1.6) was developed on twelve published models (UCE, Geneformer, scGPT, scFoundation, CellPLM, SCimilarity, CellFM, STATE, X-Cell, GEARS, CPA, CellOT) and tested on two it was not built from (TranscriptFormer, Scouter). It measures what a paper reported, not whether its results are right.

## Install

**Claude Code**

```
/plugin marketplace add leahmatzat/scfm-evidence-review
/plugin install scfm-evidence-review@scfm-tools
```

**claude.ai**: zip the folder `plugins/scfm-evidence-review/skills/scfm-evidence-review` and upload it as a skill. Once the plugin is listed in Anthropic's directory, you can add it from claude.ai directly.

## What is in this repository

| Path | What it is |
|---|---|
| `plugins/scfm-evidence-review/` | The plugin: `SKILL.md` (the rubric and instructions) and `explorer/` (the page generator and template) |
| `.claude-plugin/marketplace.json` | Lets Claude Code install the plugin straight from this repository |
| `CITATION.cff`, `.zenodo.json` | Citation and archive metadata |

See [`plugins/scfm-evidence-review/README.md`](plugins/scfm-evidence-review/README.md) for what the skill produces and what it reads and sends.

## Versions

The rubric version is in every CSV row (`rubric_version`). Releases follow it: `v1.6.0` is rubric v1.6. Each GitHub release is archived on Zenodo with its own DOI.

## Corrections and suggestions

Open an issue: a rubric rule that doesn't fit a paper, a score you think is wrong, or a check that should exist. Please include the paper, the column and task, and the page or figure.

## Cite

See `CITATION.cff`, or the Zenodo record linked from the latest release.

## Licence

Code and skill: MIT (`LICENSE`).
