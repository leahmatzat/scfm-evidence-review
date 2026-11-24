# scfm-evidence-review

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23998812.svg)](https://doi.org/10.5281/zenodo.23998812)

A Claude skill for reviewing the evidence in single-cell foundation model papers with a fixed, versioned rubric. For each paper it records which standard checks were reported, task by task, each backed by a pointer and a quote, and writes a CSV that stacks across models. An optional companion plugin, the Evidence Explorer, turns those CSVs into one offline HTML page.

The rubric (v1.7) was developed on twelve published models (UCE, Geneformer, scGPT, scFoundation, CellPLM, SCimilarity, CellFM, STATE, X-Cell, GEARS, CPA, CellOT) and tested on two it was not built from (TranscriptFormer, Scouter). It measures what a paper reported, not whether its results are right.

## Browse the audit

The scores for 14 published models, made with this skill, live in their own repository, [scfm-evidence-data](https://github.com/leahmatzat/scfm-evidence-data). Browse them task by task, with the paper's own words behind each score, in the Evidence Explorer: **https://leahmatzat.github.io/scfm-evidence-data/**

## Install

**Claude Code**

```
/plugin marketplace add leahmatzat/scfm-evidence-review
/plugin install scfm-evidence-review@scfm-tools
/plugin install scfm-evidence-explorer@scfm-tools   # optional: the Evidence Explorer page
```

**claude.ai**: zip the folder `plugins/scfm-evidence-review/skills/scfm-evidence-review` and upload it as a skill. Once the plugin is listed in Anthropic's directory, you can add it from claude.ai directly.

## What is in this repository

| Path | What it is |
|---|---|
| `plugins/scfm-evidence-review/` | The review plugin: `SKILL.md`, the rubric and instructions. Text files only; this is the folder listed in Anthropic's directory. |
| `plugins/scfm-evidence-explorer/` | The companion Explorer plugin: the page builder (`build_explorer.py`) and its HTML template. Install it from this repository. |
| `.claude-plugin/marketplace.json` | Lets Claude Code install both plugins straight from this repository |
| `CITATION.cff`, `.zenodo.json` | Citation and archive metadata |

See [`plugins/scfm-evidence-review/README.md`](plugins/scfm-evidence-review/README.md) for what the skill produces and what it reads and sends.

## Versions

The rubric version is in every CSV row (`rubric_version`). Releases follow it: `v1.7.x` is rubric v1.7, and the last number changes for fixes that leave the rubric alone. Each GitHub release is archived on Zenodo with its own DOI.

## Corrections and suggestions

Open an issue here for the rubric or the skill: a rule that doesn't fit a paper, a check that should exist, or a problem running it. Please include the paper, the column and task, and the page or figure. Corrections to a published score go to the [audit repository](https://github.com/leahmatzat/scfm-evidence-data/issues/new?template=correction.yml).

## Cite

Cite all versions with the concept DOI [10.5281/zenodo.23998812](https://doi.org/10.5281/zenodo.23998812), which always resolves to the latest release. To cite the exact version you used, take its DOI from the Zenodo record (v1.7.1: [10.5281/zenodo.24409849](https://doi.org/10.5281/zenodo.24409849)). `CITATION.cff` has the details.

## Licence

Code and skill: MIT (`LICENSE`).
