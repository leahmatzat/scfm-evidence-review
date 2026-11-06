---
name: scfm-evidence-review
description: Use when asked to review, audit or score the evidence in a single-cell foundation model paper (or a similar bio-AI model paper — cell embedding, integration, perturbation prediction). Applies the scFM audit rubric v1.6 and writes a fixed-format CSV that concatenates across models.
---

# scFM evidence review — rubric v1.6

Use this to review one paper about a single-cell foundation model, or a similar biological AI model (perturbation prediction, cell embedding, integration). The output is one Table 1 row, one Table 2 row, and a short list of flags, each backed by a quote from the paper.

The rubric was built from a 12-model audit (UCE, Geneformer, scGPT, scFoundation, CellPLM, SCimilarity, CellFM, STATE, X-Cell, GEARS, CPA, CellOT) and tested on two papers it was not built from (TranscriptFormer, Scouter). It measures **completeness of reporting**, not quality of science.

**Model:** use the strongest available model (in the audit, Claude Opus). A smaller model matched it on the per-model scores but found far fewer per-task problems and contradicted claims, mostly because it read less of each paper.

## Principles — read first

1. **Nobody is doing anything wrong.** Describe accurately and attribute charitably. No moral vocabulary. The one exception: a stated claim that isn't true is said plainly.
2. **Score the fact, record the judgment.** Every score answers a countable question. Opinions about how good something is go in the recorded fields, never in the number.
3. **Every score is a floor, not a ceiling.** A 2 means the paper protected the claim against one known way of being empty. It does not mean the claim is true. A 0 means a check wasn't reported, never that a result is wrong.
4. **Exposure, not effect.** If evaluation data appears in a pretraining corpus, report the overlap. Do not claim the result is inflated unless the paper measured that.
5. **Every entry needs a source pointer:** paper version · section or figure · a short quote. An entry without a pointer is not finished.
6. **Never fill a gap by inference.** If you haven't read it, mark it `[V]`. "Not found" is only allowed after the full search in step 2.

## Step 1 — Identify what you are scoring

- Find every version: preprint(s), published article, supplementary information, peer-review file (Nature journals publish these), code repository, model card.
- **Score the peer-reviewed published version** — not just a publicly available one. A preprint is public but not peer reviewed. Record the version and its peer-review status in **Source scored** (e.g. *Nature Methods* 2024, peer reviewed · bioRxiv v4, not peer reviewed). If only a preprint exists or could be read, say so. If versions differ in ways that change a score (new ablations, new tasks, new baselines), add ⚠ and note what differs. Preprint servers often don't link to the published version — look up the DOI directly.
- **If the published main text can't be read but its supplement can** (e.g. a paywalled article with a free supplement), score the latest preprint for the main text and figures and the published supplement for everything else. Set `source_scored` to name both (e.g. `bioRxiv v2 (2025-10-11) main text + Science 2026 Supplementary Materials`) and `peer_reviewed` to `no`, because the main text read was not peer reviewed. In `version_difference`, compare the preprint's methods and supplement with the published supplement and say that the published main text was not read.
- **Enumerate all supplementary files** before scoring. In the original audit, a corpus manifest, an identity baseline and a leakage ablation each lived only in a supplement that the main text never mentioned.
- Note which **model variant or checkpoint** produced which number. Several papers report headline results from different sizes of "the same" model.

## Step 2 — How to read (the reading guide)

**Do not rely on keyword search for controls.** In the original audit, searching for words like "control", "baseline" or "random" missed a real control in every paper read in full. Controls appear under other names, for example:
- a "Random" arm · "two models" · "model ablation" · "feature permutation" · "alternative methods"
- an arm named by its inputs, like "ST+HVG" (a model trained on raw genes instead of embeddings)
- a "trivial identity" baseline in a supplementary figure

Read the Methods, every results figure, and every supplementary figure caption. For each claim the paper makes, ask what it was compared against.

**Pages with no text layer must be viewed, not skipped.** Reporting summaries, scanned supplements and figure-only pages often extract as blank text. Open them as images and read them. In the original audit, several contradicted claims sat only in image-only reporting summaries and figure panels, and a run that skipped them missed every one. If a page truly can't be read, list it under `unverified`.

Also check:
- **Repository flags and README.** User-facing options (pooling type, which checkpoint) are sometimes documented only there.
- **The availability statement is a claim.** Check that the repo, weights and data actually exist, and record the date you checked.
- **Where fixes live.** Problems raised in review are often addressed in supplementary material while the headline figures stay unchanged. Record where the relevant evidence sits (main text vs supplement).
- **Search the peer review file for methods details.** Authors' replies to reviewers often state things the paper never does (e.g. which data hyperparameters were tuned on). Before scoring any column as 1 or 0 because a detail is "not stated", search the peer review file too, and cite it if the answer is there.

## Step 3 — Table 1: what the model is (facts, not scored)

Record each with a source pointer:

- **Class** — representation · perturbation · both. Note if perturbation prediction runs through someone else's model plugged in (e.g. embeddings fed into GEARS).
- **Perturbation type** — genetic · chemical · signaling.
- **Architecture** and **training objective** (masked / generative / supervised / distribution matching; does it need labels? Note any label hierarchy or ontology used to shape the loss or choose training examples).
- **Context / structure** — implicit (learned from data only) · explicit conditioning (cell type, batch, dose supplied) · structured prior (external biology injected: gene graph, protein embeddings, knowledge bases).
- **Knowledge source** (`knowledge_source`) — where the model's knowledge comes from. Start `value` with `Sources:` and every source that applies, joined by ` + `, then a full stop and one line of detail:
  - `expression` — measured data (expression, imaging, spatial coordinates) learned by the model itself
  - `sequence` — protein or DNA sequence models (e.g. ESM embeddings of each gene's protein)
  - `curated` — knowledge bases, ontologies, graphs, chemical structure, or other external datasets (GO, STRING, Cell Ontology, DepMap, molecular fingerprints)
  - `text` — anything read by a language model: written gene descriptions turned into embeddings, LLM embeddings, or a language-model backbone that reads cells as text
  - Example: `Sources: expression + text. Measured expression plus GenePT embeddings of NCBI gene descriptions.` Include knowledge that only shapes training (e.g. an ontology used for triplet sampling) and say so in the detail.
  - **Why `text` matters:** the text, or the language model's own training data, may already describe the experiments the model is tested on, and with a closed language model nobody can check. It is a fact about how the model is built, not a penalty.
- **Model variants** — sizes, checkpoints, which produced which result.
- **Embedding extraction** — what is pooled, from where, at what dimension.
- **Scale** — cells and parameters. If two numbers appear, check whether they describe two different corpora before calling it an inconsistency.
- **Gene coverage** (feature space) — all genes · fixed vocabulary · genes measured in every dataset · highly variable genes (HVGs) chosen per dataset. Record the gene count.
- **Data modality** and **organism**.
- **Availability** — openness checklist (date checked): weights · inference / fine-tuning code · pretraining code · preprocessing specified · training corpus downloadable · corpus manifest (keyed by accession or by citation) · licence (permissive / non-commercial / revocable) · status (released / declared-incomplete / declared-unfulfilled).
- **Run-to-run spread** (was V5, a fact since v1.5) — for each evaluated task family, was dispersion (SD, CI, seeds, splits, folds, bootstraps) reported on that family's headline result? Write `k of n task families`, then which have it and which don't (task IDs from below), and the kind (split / seed / bootstrap).
- **What was held out** — the evaluation's held-out axes: cells · donors · studies · cell types · perturbations · tissues · species · platforms.
- **Independent evaluations** — independent papers that evaluated the model, and what they found (agreed / mixed / contradicted). "None yet" is a valid entry.
- **Evaluated tasks** — the fixed task list, by family: annotation · integration · reference mapping / retrieval · zero-shot embedding · denoising / imputation · perturbation prediction (genetic / chemical / signaling) · reverse perturbation · drug response · gene-level prediction · gene programs / GRN. A task = an evaluation reported with its own dataset and metric.
- **Task names in the output** — use exactly these IDs in the `task` column: `annotation` · `integration` · `reference_mapping` · `zero_shot_embedding` · `denoising` · `perturbation_genetic` · `perturbation_chemical` · `perturbation_signaling` · `reverse_perturbation` · `drug_response` · `gene_level` · `gene_programs`. If one family has several distinct evaluations that score differently, add a short qualifier after a colon (e.g. `perturbation_genetic:combinations`). A task outside every family: `other:<short_name>`.
- **Gates** (yes/no, with pointer): pretraining stage? · injected external prior? · biological claim made? · attribution claim made?

The gates decide whether a Table 2 column applies. **n/a is a lookup, not a judgment:** if the gate is "no", the column is n/a.

## Step 4 — Table 2: what the paper reported

Score each column 2 / 1 / 0 / n/a. Fill the recorded fields. Column names are reader-facing; the short codes in brackets are the audit's internal IDs.

### Simple baseline (V1)
*Reader's question: Does it beat something simple — on the task I care about?*
- **Fact:** on this task, was a simple, non-deep baseline run (linear / additive, mean-shift, PCA, raw or HVG expression, logistic regression / SVM, tree ensembles such as random forest or XGBoost, Harmony-type)? Any non-deep method counts.
- **Score every evaluated task separately**, like Input dependence, Training-data overlap and Fair test number.
- **2** a simple non-deep baseline was run on this task · **1** only a trivial reference on this task (no-change / identity, random subset, random classifier, chance) · **0** deep comparators only, or no comparator.
- **Outcome (required, per task):** start `value` with `Outcome:` and one of — `beat` (the model is better than the best simple baseline on the paper's headline metric for this task) · `tied` (within the paper's reported spread, or described as comparable) · `lost` (the simple baseline is better) · `mixed` (better on some metrics or datasets, worse on others — say which) · `not reported` (run but numbers not shown) · `none` (score 0). Judge the outcome against the **strongest baseline run on the task, trivial references included** (if the no-change prediction beats the model, the outcome is `lost` even when a simple baseline lost too). Use the paper's own numbers. **Look for them in source data files and supplementary tables before relying on the authors' description** — baseline numbers are often there even when the figure is only an image. If the numbers exist only in a figure image, record the outcome from the text and mark it `[V]`.
- **Record:** baseline names · whether baselines were tuned (matched / defaults / unstated) · field-standard baseline flag: did the paper run the baseline the field had established as necessary for this task by its publication date? (This is how a paper gets credit for meeting the standard of its time; it is a note, not part of the score.)
- Chance-level references count here (score 1), not in Input dependence. **A chance line drawn on a plot counts** when it is labelled and plotted against the model's result (e.g. AUC = 0.5 on the model's ROC panel), even if the text never discusses it.
- **A baseline built on a pretrained deep model's features is deep**, even when it needs no training of its own (e.g. averaging frozen protein-language-model vectors over a cell's expressed genes). "Simple" means no learned deep representation anywhere in the baseline.
- **A reference used to define or select what is being evaluated is not a comparison.** If the candidates are defined as those that beat the reference (e.g. genes kept because they shift cells more than random genes do), they beat it by construction: score **0**, `Outcome: none`, and say why in the value.

### Input dependence (V2)
*Reader's question: Does the output depend on real signal in the input?*
- **Fact:** on this task, was a model input corrupted at inference (shuffled labels, scrambled expression, permuted embeddings), or an input supplied that should produce no effect?
- **Score every evaluated task separately**, like Simple baseline. A check on one task says nothing about another (the same logic as partial-input baselines in NLP and randomisation sanity checks in vision).
- **2** done on this task, with the degradation (or the absence of a false effect) measured · **1** done on this task but not measured (shown only, e.g. a UMAP) · **0** none on this task.
- **Record:** family — **corruption** (destroy the input, confirm collapse; suits perturbation models) or **specificity** (should-be-null input, confirm no effect; suits representation and integration models) · what was corrupted.
- **Not V2:** retraining without an input (a design ablation) · corruption used as the training task · permutation tests that validate a dataset rather than the model · chance-corrected metrics like ARI.
- If what was corrupted is an injected biological prior, it is **Prior dependence**, not Input dependence. Never both.

### Pretraining payoff (B-init) ⟨gate: pretraining stage⟩
*Reader's question: Does pretraining earn its keep?*
- **Fact:** what else changed between the pretrained arm and the no-pretraining arm? List the differences.
- **2** an arm exists and only pretraining differs · **1** an arm exists but other things also changed (model size, frozen vs trained, graph type, …) · **0** the model is pretrained, but no comparison to a non-pretrained version is reported · **n/a** no pretraining stage.
- **Record:** variables that moved · scope (which tasks) · control type (the model against its untrained self, or embeddings swapped into a host model).
- Differences that follow necessarily from removing pretraining are recorded, not scored.

### Unwanted variation (B-sys)
*Reader's question: Is the result separated from batch, donor, lab and other non-biological effects?*
- **Fact:** were nuisance axes (batch · donor · study · platform · preservation) **evaluated**, not just modelled?
- **2** evaluated · **1** modelled or partly addressed, effect not tested · **0** none · **n/a** pure representation model with no perturbation or integration evaluation.
- **Record:** which axes · community convention (e.g. scIB metrics) or a bespoke design.

### Prior dependence (B-scr) ⟨gate: injected external prior⟩
*Reader's question: Does the injected biology actually matter?*
- **What counts as an injected prior:** external information the model **takes in** as input, weights or graph, at training or inference (gene graphs, protein or text embeddings, knowledge-base features, molecular fingerprints). A label hierarchy or ontology used only to shape the training loss or choose training examples is **part of the training objective**, not a prior: record it in Table 1 `training_objective`, and the gate stays no for it.
- **Fact:** was each injected prior scrambled?
- **2** every injected prior · **1** some (record n of N) · **0** none · **n/a** no injected prior.
- **Record:** which priors · full vs graded permutation (a within-cluster permutation separates "uses gene identity" from "uses similarity structure") · what happened.
- **Text-derived inputs:** if `knowledge_source` includes `text`, always end this column's value with an exposure note marked [V]: the text, or the language model's training data, may describe the evaluation experiments and can't be checked. Scrambling the text tests whether the model *uses* it; it cannot show whether the text already *contains* the answers. The note is not scored.

### Training-data overlap (Leakage) ⟨gate: pretraining stage⟩
*Reader's question: Was the test data in the training data?*
- **Fact:** did the paper state that evaluation data was excluded from pretraining, **or measure the effect of including it** (e.g. training with and without the evaluation data and comparing)?
- **2** stated or measured for this task · **1** partly (some of the task's datasets) · **0** neither · **n/a** no pretraining stage.
- **Score every evaluated task separately — per-task rows only, no `all` row.**
- Record how any effect was measured, on which tasks, and what it found.
- **Record, per task:** the corpus-check result — clean / exposure found / not checkable — with a pointer.
  - If a corpus-checker registry entry exists for the model, use it and cite it.
  - **If not, check by hand with what is available:** find the evaluation datasets' accession numbers (GEO, ArrayExpress, CELLxGENE IDs) and search the published corpus manifest or supplementary data tables for them. If the manifest is keyed by citation rather than accession, match on the citing study. Record what you searched and how.
  - If no manifest is published, the result is "not checkable".
- **What counts as a match:** the same dataset ID or accession, or the same study with an exact cell count for the same tissue. Anything weaker is not a match. If none of these can be checked with what is available, the result is "not checkable", marked [V].
- **Models with no pretraining stage but an injected prior** (e.g. gene embeddings from a language model): this column is n/a. If the prior's own training data could contain the evaluation data, record that under Prior dependence, marked [V]; it is not scored. If the model's own backbone is a pretrained language model, its pretraining text is part of the model's pretraining: score this column as usual, and the corpus check is "not checkable" unless that corpus is published.
- If the paper states exclusion and the corpus check finds overlap, say so plainly. Report exposure, not effect.

### Fair test number (Selection hygiene)
*Reader's question: Would you get this number on your own data?*
In one line: did the authors pick their genes or their settings by looking at the answers they were then graded on?
- **Fact:** were any **setup decisions** made using the **test answers**?
- **Setup decisions** — decisions made while building or evaluating the model that change the reported number:
  1. **Feature and preprocessing decisions:** which genes go in (HVG or feature selection); anything fitted to the data (normalisation statistics, scaling, PCA).
  2. **Model selection decisions:** hyperparameters; which model version, checkpoint or epoch to keep; early stopping; thresholds or cut-offs; pooling or embedding method when picked by results.
- **Test answers** — information about the test set a real user would not have when applying the model to new data: **labels** (cell types, conditions, annotations) · **the measured outcome the model predicts** (for a perturbation model, the perturbed cells' expression) · **performance scores on the test set**. Unlabeled test **inputs** a user would also have (e.g. query expression for integration or annotation) are **not** answers.
- **2** every reported setup decision was made without test answers — on training or validation data, on unlabeled inputs only, fixed in advance, or by a stated rule of thumb · **1** a setup decision is reported without saying what data it used, so you can't tell whether answers were involved (quote the sentence) · **0** a setup decision used test answers.
- **Kind (required for every 0):** start `value` with `Kind:` and one or both of —
  - `model selection` — a model-selection decision (hyperparameters, checkpoint or epoch, threshold, pooling, which of several settings to report) was made by looking at test labels or test scores, **or the model's allowed outputs were restricted to the test set's own label set** (a user predicting on new data would not have those labels). This directly favours the reported number.
  - `features` — a feature or preprocessing decision (HVGs, normalisation, PCA fitted to data) saw the test answers (e.g. HVGs computed including held-out perturbed cells). This leaks information indirectly; the size of the effect is usually unknown.
- **A setting stated with no source** (e.g. "C = 0.01", "k = 10", "trained for 8 epochs"): score **1** unless the paper says how it was set: chosen in advance or not tuned, a library or tool default, a stated rule of thumb, or chosen on validation data. Then it can score 2. Don't infer "fixed in advance" from a value being the same across tasks (principle 6).
- **Settings chosen on validation data across repeated random splits:** score what the paper states (validation data). If the design would allow one split's validation items to be another split's test items but nobody shows it, say so in the value and don't lower the score (principle 6).
- **Not a setup decision:** a cut-off that **defines the ground truth** — set by a stated rule, applied the same way to the true data and to every model compared (e.g. thresholds reconstructing the original study's labels). It can score 2 if the rule is stated.
- **Score every evaluated task separately** (e.g. `integration 2 · perturbation 0`). Per-task columns are reported per task; they are not collapsed to one number per model.
- **Record:** each setup decision, with its quote and the data it used · split unit (cell / donor / study / perturbation / …) · split provenance (standard published split vs bespoke) · any disclosure or measurement of answer use, as a bonus (a disclosed, measured leak still scores as it stands).
- **Not this column:** whether test data was inside the training or pretraining data — that is Training-data overlap. Frozen statistics from a pretraining corpus are not a setup decision here.
- Search cues: "highly variable", `scanpy.pp.highly_variable_genes`, "feature selection", "selected", "best", "optimal", "validation", "tuned", "sweep", "early stopping", "checkpoint".
- Common pattern (perturbation models): HVGs computed on the full dataset including held-out perturbed cells — the perturbed expression is the answer, so this scores 0.
- Common pattern: a model chosen as "best on the validation studies", with the headline reported on those same studies — test scores were used, so this scores 0. The fix is a third split.

### Explanation check (T2) ⟨gate: attribution claim⟩
*Reader's question: Was the model's explanation of itself tested?*
Attribution = the paper's explanation of what the model learned: attention maps, gene embeddings, gene programs, saliency, **and claims that the model's representation encodes biology** (e.g. cell embeddings organised by lineage or ontology) — these are probing claims, and their model-free baseline is a baseline representation such as PCA or raw expression.
- **Claims about frozen outside inputs are not attribution.** If the gene embeddings come from another model and are not changed in training, claims about them describe the input, not what this model learned.
- **No double counting:** a result already scored as a task in Table 2 (e.g. a reference-mapping or integration benchmark) cannot also be the evidence here. Use the claim's own evidence.
- **Score the strongest attribution claim** by the highest rung it reaches:
  - **2** beats a **model-free baseline** (co-expression, correlation, gene-level statistics like expression level or variance — a random-gene null does not count), **or** shows an effect under **intervention on the model itself** (ablating components or attention heads, permuting priors or internal representations)
  - **1** matches known biology in an external reference (ChIP, TRRUST, Reactome, marker lists). This includes input interventions whose effects are checked against a reference — e.g. in silico gene deletion compared with ChIP targets. Record whether the result is graded (effect scales with target confidence).
  - **0** shown only, or compared only to a positive control
  - **n/a** no attribution claim
- **Record:** every claim and its rung · hit rate vs graded result (does the effect scale with target confidence?) · background rate given? · independence of the reference (was it also an input?) · external evaluations bearing on it.
- If the strongest claim isn't the paper's headline claim, say so in this column's value (which claim is the headline, which is strongest, and where each sits).
- Known caution: attention-derived gene networks can track co-expression and simple gene statistics (Kendiukhov, arXiv 2602.17532, preprint). A rank-based model's deletion effects may partly track expression level — check whether the paper controls for it.

### Biological validation (BV) ⟨gate: biological claim⟩
*Reader's question: Was a claim about biology checked outside the model?*
A biological claim asserts something true about biology, beyond benchmark accuracy ("these examples support the validity of our predictions"). Read for the claim itself, not a keyword.
- **Fact:** the timing of the validation.
- **2** a prediction was tested in a new experiment · **1** checked against outside evidence that already existed · **0** a claim was made, supported only by the model's own benchmarks · **n/a** no biological claim.
- **Record:**
  1. **Timing** — new experiment, or existing data?
  2. **Independence** — was the validating evidence already inside the model: in its priors (e.g. STRING, DepMap, GO), its training corpus, or its training labels? Agreement with something the model was given is weaker evidence.
  3. **Selection** — were all predictions checked, with a denominator, or a few examples chosen to show?
  4. **Evidence type** — wet lab · orthogonal assay · curated database · literature.

### Explanation check vs Biological validation — the most confusable pair
- T2 checks the model's explanation **of itself**. BV checks a claim **about the world**.
- Test: if the validation failed, would you conclude "we don't understand how it works" (T2) or "its biology claims are wrong" (BV)?
- The noun: attention, embeddings, gene programs → T2. Predictions, discoveries, candidates → BV.
- Never count one analysis in both.

### Not scored
The authors' own architecture or objective ablations (layer counts, loss terms, set sizes). They are standard in ML and don't discriminate between papers. Record them in notes.

## Step 5 — Output (fixed format)

Every run produces **one CSV file** in long format: one row per field. Files from different runs share the same header, so they can be stacked into one large table (keep the first file's header, drop the rest).

**File name:** `<model>_<YYYY-MM-DD>.csv` (e.g. `ExampleFM_2026-10-06.csv`). Save it in the working folder.

**Header (exactly this, in this order):**
```
run_id,rubric_version,run_date,scorer,model,source_scored,peer_reviewed,table,field,task,score,value,pointer,flags
```

| Column | What goes in it |
|---|---|
| run_id | `<model>_<YYYY-MM-DD>` — same as the file name |
| rubric_version | `v1.6` |
| run_date | YYYY-MM-DD |
| scorer | who ran it — the AI model name and version (e.g. `claude-opus-5-5`) or a person's initials |
| model | the model being reviewed, spelled as in the field list below |
| source_scored | journal or server, year, version (e.g. `Nature Methods 2024` · `bioRxiv v4`) |
| peer_reviewed | `yes` / `no` |
| table | `T1` · `T2` · `flag` |
| field | one ID from the fixed list below — never invent a new one |
| task | `all`, or a task ID from the list in Step 3. **Simple baseline, Input dependence, Training-data overlap and Fair test number get one row per task and no `all` row.** Every other column uses `all` |
| score | T2: `2` `1` `0` `n/a`. T1: leave blank. Flags: leave blank |
| value | the fact or recorded fields, in plain words. For T2, start with a one-line reason for the score |
| pointer | `version · section/figure · "short quote"`. Use `[V]` if not read |
| flags | semicolon-separated; blank if none |

**Formatting rules:** wrap every value in double quotes; write a quote mark inside a value as two quote marks (`""`); no line breaks inside a value; one row per field (per task where required). Every field in the list gets a row, even if the value is `[V]` or `n/a`.

**Fixed field IDs**

- **T1:** `class` · `perturbation_type` · `architecture` · `training_objective` · `context_structure` · `model_variants` · `embedding_extraction` · `scale` · `gene_coverage` · `data_modality` · `organism` · `availability_weights` · `availability_inference_code` · `availability_pretraining_code` · `availability_preprocessing` · `availability_corpus` · `availability_manifest` · `availability_licence` · `availability_status` · `availability_date_checked` · `knowledge_source` · `run_to_run_spread` · `what_was_held_out` · `independent_evaluations` · `evaluated_tasks` · `gate_pretraining` · `gate_injected_prior` · `gate_biological_claim` · `gate_attribution_claim`
- **T2:** `simple_baseline` *(per task)* · `input_dependence` *(per task)* · `pretraining_payoff` · `unwanted_variation` · `prior_dependence` · `training_data_overlap` *(per task)* · `fair_test_number` *(per task)* · `explanation_check` · `biological_validation`
- **flag:** `version_difference` · `claim_contradicted` · `unverified` · `note` *(a fact no column holds)* · `observations`
  - `claim_contradicted` = a statement **in the paper itself** that the paper's own data, supplement or manifest contradicts (principle 1: say it plainly). Disagreement from **independent evaluations** is not this flag — it goes in `independent_evaluations`. **Never cite an outside paper in a `claim_contradicted` row**; if a claim is contradicted only by outside work, it belongs in `independent_evaluations` alone. **An internal number slip** (a p-value or count that differs between text and figure) goes in `note` unless it changes a number a reader would rely on; then it is `claim_contradicted`. Before flagging a methods sentence as contradicted, check whether the Results state the method correctly: if they do, it is an `observations` item.
  - `observations` = the reviewer's comments: things a reader should know that are judgment rather than countable fact (e.g. the strongest evidence sits in a supplement the main text never cites; the headline uses a different model size from the other results; a baseline is mentioned in the rebuttal but not shown). One row, up to five items, each starting `Observation:` and separated by ` | `, each with its own pointer in the `pointer` column (same order). Principle 1 applies: describe, don't accuse. Observations never change a score, and a score never depends on one. Leave the value blank if there is nothing to add.

**Example rows** *(a made-up model, to show the format only)*
```
"ExampleFM_2026-10-06","v1.6","2026-10-06","claude-opus-5-5","ExampleFM","Journal X 2025","yes","T2","pretraining_payoff","all","1","Arm exists but model size also changes: the from-scratch arm is smaller. Scope: 2 of 4 tasks.","Journal X 2025 · Suppl. Note 3 · ""the from-scratch model has 4 layers""",""
"ExampleFM_2026-10-06","v1.6","2026-10-06","claude-opus-5-5","ExampleFM","Journal X 2025","yes","T2","fair_test_number","annotation","2","Genes chosen by presence in all datasets; hyperparameters chosen on a separate validation split. No test labels used.","Journal X 2025 · Methods · ""selected on the validation set""",""
"ExampleFM_2026-10-06","v1.6","2026-10-06","claude-opus-5-5","ExampleFM","Journal X 2025","yes","T2","simple_baseline","integration","2","Outcome: tied. PCA on HVGs run; overall score 0.61 vs ExampleFM 0.62, within the reported SD. Baselines at defaults.","Journal X 2025 · Suppl. Table 4 · ""PCA (HVG)""",""
"ExampleFM_2026-10-06","v1.6","2026-10-06","claude-opus-5-5","ExampleFM","Journal X 2025","yes","T2","fair_test_number","perturbation_genetic","0","Kind: features. HVGs computed on the full dataset, including held-out perturbed cells.","Journal X 2025 · Methods · ""top 5,000 highly variable genes""",""
"ExampleFM_2026-10-06","v1.6","2026-10-06","claude-opus-5-5","ExampleFM","Journal X 2025","yes","flag","version_difference","all","","Published version adds an ablation absent from the preprint.","bioRxiv v2 vs Journal X 2025",""
```
*(Examples show the format only. Do not copy their content.)*

**After writing the file**, show a short summary in the conversation: the Table 2 scores as one line per column, then the flags. Keep the CSV as the record. Then offer the explorer (Step 6).

Keep the language plain. Quote the paper rather than paraphrasing where a score depends on wording. Cross-model patterns belong in the findings document, not in `note` rows.

## Step 6 — The Evidence Explorer (optional, for the reader)

The CSV is the record. A reader usually wants something easier to look through, so after the summary offer to build the **Evidence Explorer**: one self-contained HTML page with two views.
- **By task:** the reader picks a task family ("I want a model for genetic perturbation"). Each model evaluated on it shows its per-task checks, then the whole-model checks. Clicking any score opens the question, the reason and the paper's own words.
- **Badge:** models whose `knowledge_source` includes `text` carry a "Text-derived inputs" badge, explained in the model card.
- **Compare models:** every scored model side by side. One table shows what each model was evaluated on (count of evaluations per task family). The other shows the checks: counts of 2/1/0 for the per-task columns, never an average; one score each for the whole-model columns; run-to-run spread; any contradicted claim.

**Build it** with the script in `explorer/` next to this file (standard-library Python, no internet needed):
```
python3 explorer/build_explorer.py <folder>/*.csv --out evidence_explorer.html
```
Give it every CSV the reader has scored, not only today's: the page always shows all models it is given, and if a model appears in several runs it keeps the newest run. Add `--note "Private draft"` to print a line under the title. If `explorer/` is missing, say so and offer the CSV and the summary instead; don't hand-build a different page.

**What the reader can keep.** The page is a file. Open it in any browser, offline, as often as they like; save it, email it. It holds its own data, so nothing needs regenerating to look at it again. Rebuild only after scoring another model, by rerunning the same command over the folder. Buttons on the page: **Download scores (CSV)** saves the scores it contains, and **Print or save as PDF** prints the current view (landscape). A link ending in `#compare` or `#<task family>` opens that view directly.

Before anyone shares the page, remind them that it shows the reviewer's reading of other groups' papers: principle 1 applies to how it is described.

## When re-scoring a model that has been scored before

Score blind: do not look at earlier scores until your row is finished. Then compare, and record every difference as old → new, with the date and the reason. A disagreement is data about the rubric, not an error to hide.
