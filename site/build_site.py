#!/usr/bin/env python3
"""Build the public Evidence Explorer (docs/index.html) from data/final_scores_v1.7.csv.

Uses the Explorer plugin's builder, then adds what only the public page needs:
a "Suggest a correction" link on every score and model card (opens a GitHub issue form),
and a footer with the licence and repository link.

Usage (from the repository root):
    python3 site/build_site.py
"""
import glob, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = "https://github.com/leahmatzat/scfm-evidence-review"
BUILDER = os.path.join(ROOT, "plugins/scfm-evidence-explorer/skills/scfm-evidence-explorer/build_explorer.py")

csvs = sorted(glob.glob(os.path.join(ROOT, "data", "final_scores_v*.csv")))
if not csvs:
    sys.exit("No data/final_scores_v*.csv found.")
out = os.path.join(ROOT, "docs", "index.html")
subprocess.run([sys.executable, "-I", BUILDER, csvs[-1], "--out", out], check=True)

page = open(out, encoding="utf-8").read()

FIX_JS = f"""
function fixUrl(m,f,t){{
  const q = new URLSearchParams({{template:'correction.yml', title:`[Correction] ${{m}} · ${{(COL[f]&&COL[f].name)||f}}${{t&&t!=='all'?' · '+t:''}}`, model:m, column:(COL[f]&&COL[f].name)||f, task:t||'all'}});
  return '{REPO}/issues/new?' + q.toString();
}}
function fixLink(m,f,t){{ return `<div class="sec"><a class="fix" href="${{fixUrl(m,f,t)}}" target="_blank" rel="noopener">Suggest a correction on GitHub</a></div>`; }}
"""
anchors = {
    "function scoreDetail(m,f,t){": FIX_JS + "\nfunction scoreDetail(m,f,t){",
    "${r.fl?`<div class=\"sec\"><h3>Flags</h3><p>${esc(r.fl)}</p></div>`:''}`);":
        "${r.fl?`<div class=\"sec\"><h3>Flags</h3><p>${esc(r.fl)}</p></div>`:''}` + fixLink(m,f,t));",
    "<h3>Version differences</h3><p>${esc(d.flags.version_difference.v)}</p></div>`:''}`);":
        "<h3>Version differences</h3><p>${esc(d.flags.version_difference.v)}</p></div>`:''}` + fixLink(m,'model card','all'));",
    "</footer>": (f" Data licensed <a href=\"https://creativecommons.org/licenses/by/4.0/\">CC BY 4.0</a>; download it from the "
                  f"<a href=\"{REPO}/tree/main/data\">repository</a>. The rubric and skill are at <a href=\"{REPO}\">github.com/leahmatzat/scfm-evidence-review</a>. "
                  f"Spotted something wrong? Open any score and use <i>Suggest a correction</i>, or <a href=\"{REPO}/issues/new?template=correction.yml\">open an issue</a>.</footer>"),
    "</style>": ".fix{font-size:14px;font-weight:600;color:var(--accent)}footer a{color:inherit}\n</style>",
}
for a, b in anchors.items():
    if page.count(a) != 1:
        sys.exit(f"anchor found {page.count(a)}x: {a[:60]}")
    page = page.replace(a, b)
page = page.replace("<title>", "<title>", 1)
open(out, "w", encoding="utf-8").write(page)
print("docs/index.html written")
