# scFM Evidence Explorer

A companion to [scFM Evidence Review](https://github.com/leahmatzat/scfm-evidence-review/tree/main/plugins/scfm-evidence-review). It turns the CSVs that skill writes into one self-contained HTML page: every model you have scored, by task family and side by side. The page opens offline in any browser and holds its own data, so you can keep it, email it or print it.

It ships as its own plugin because it includes a Python script and an HTML template. Claude's plugin directory accepts only text files from individual publishers, so the directory lists the review skill alone. Install this one from this repository.

## Install (Claude Code)

```
/plugin marketplace add leahmatzat/scfm-evidence-review
/plugin install scfm-evidence-explorer@scfm-tools
```

## How to use it

After scoring one or more papers with scfm-evidence-review, ask Claude to *"build the Evidence Explorer from my CSVs"*. Or run the script yourself from the plugin folder:

```
python3 skills/scfm-evidence-explorer/build_explorer.py <folder>/*.csv --out evidence_explorer.html
```

Give it every CSV you have scored. If a model appears in several runs, the page keeps the newest run.

## What it reads, runs and sends

- **Reads** only the CSVs you give it.
- **Runs** `build_explorer.py` (Python standard library only), only when you ask for the page.
- **Writes** one HTML file, where you tell it to.
- **Sends** nothing anywhere. The page makes no network requests.

## Licence

MIT. See `LICENSE`.
