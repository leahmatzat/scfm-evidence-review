#!/usr/bin/env python3
"""Build the Evidence Explorer: one self-contained HTML page from scfm-evidence-review CSVs.

The page needs no server and no internet. Open it in any browser, keep it, email it.
Rebuild it only when you score another model (it always reads every CSV you give it).

Usage:
    python3 build_explorer.py output/*.csv --out evidence_explorer.html
    python3 build_explorer.py final_scores_v1.5.csv --out evidence_explorer.html --note "Private draft"

Standard library only. The template (explorer_template.html) must sit next to this script,
or be given with --template.
"""
import argparse, csv, datetime, html, json, os, re, sys

T1_SKIP = set()


def clean(s):
    return re.sub(r'""', '"', (s or "").strip())


def load(paths):
    rows = []
    for p in paths:
        with open(p, newline="", encoding="utf-8") as f:
            rows += list(csv.DictReader(f))
    return rows


def build_data(rows):
    data, latest = {}, {}
    # if the same model appears in several runs, keep only its newest run
    for r in rows:
        m, d = r["model"], r.get("run_date", "")
        if d >= latest.get(m, ""):
            latest[m] = d
    for r in rows:
        m = r["model"]
        if r.get("run_date", "") != latest[m]:
            continue
        d = data.setdefault(m, {"source": clean(r["source_scored"]), "peer": clean(r["peer_reviewed"]), "t1": {}, "t2": [], "flags": {}})
        tab, field = r["table"].strip(), r["field"].strip()
        v, p = clean(r["value"]), clean(r["pointer"])
        if tab == "T1" and field not in T1_SKIP:
            d["t1"][field] = {"v": v, "p": p}
        elif tab == "T2":
            d["t2"].append({"f": field, "t": r["task"].strip(), "s": r["score"].strip(), "v": v, "p": p, "fl": clean(r.get("flags", ""))})
        elif tab == "flag":
            if field in d["flags"]:  # several rows of one flag (e.g. two contradicted claims)
                d["flags"][field]["v"] += " | " + v
                d["flags"][field]["p"] += " | " + p
            else:
                d["flags"][field] = {"v": v, "p": p}
    return dict(sorted(data.items(), key=lambda kv: kv[0].lower())), latest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="+")
    ap.add_argument("--out", default="evidence_explorer.html")
    ap.add_argument("--template", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "explorer_template.html"))
    ap.add_argument("--note", default="", help="optional line shown under the title, e.g. 'Private draft'")
    a = ap.parse_args()

    rows = load(a.csv)
    if not rows:
        sys.exit("No rows found.")
    data, latest = build_data(rows)
    versions = sorted({r["rubric_version"] for r in rows if r["model"] in data})
    scorers = sorted({r["scorer"].split(" (")[0] for r in rows if r["model"] in data})
    dates = sorted(v for v in latest.values() if v)
    span = dates[0] if dates and dates[0] == dates[-1] else (f"{dates[0]} to {dates[-1]}" if dates else "")

    meta = [f"<span><b>{len(data)} model{'s' if len(data) != 1 else ''}</b></span>",
            f"<span>Rubric {html.escape(', '.join(versions))}</span>",
            f"<span>Scored {html.escape(span)} by {html.escape(', '.join(scorers))}</span>"]
    if a.note:
        meta.append(f"<span>{html.escape(a.note)}</span>")

    page = open(a.template, encoding="utf-8").read()
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    src = ", ".join(os.path.basename(p) for p in a.csv) if len(a.csv) <= 3 else f"{len(a.csv)} CSV files"
    page = (page.replace("__DATA__", blob).replace("__META__", "".join(meta))
                .replace("__BUILT__", datetime.date.today().isoformat()).replace("__SOURCE__", html.escape(src)))
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"{len(data)} models → {a.out}")


if __name__ == "__main__":
    main()
