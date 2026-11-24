# v1.7 targeted recheck — 2026-11-24

No scores changed. 988 rows, 14 models.

| Model | Field | Task | Change | Detail |
|---|---|---|---|---|
| CellFM | claim_contradicted | all | row moved to note | number slip; conclusion vs SVM unchanged and the slip understates CellFM's margin |
| SCimilarity | claim_contradicted | all | edited | caption threshold slip (<50 vs <33) |
| Geneformer | claim_contradicted | all | edited | internal inconsistencies moved to note; field reads none found |
| CellPLM | claim_contradicted | all | edited | parts 2 (appendix ablation wording) and 3 (corpus cell count) are slips -> note; part 1 stays |
| CellFM | training_data_overlap | perturbation_chemical | edited | corpus match |
| CellPLM | training_data_overlap | zero_shot_embedding | edited | corpus match |
| CellPLM | training_data_overlap | denoising | edited | corpus match |
| CellPLM | training_data_overlap | perturbation_genetic | edited | corpus match |
| Geneformer | training_data_overlap | annotation | edited | corpus match |
| Geneformer | training_data_overlap | annotation:cardiomyopathy_state | edited | corpus match |
| Geneformer | training_data_overlap | gene_level:n1_centrality | edited | corpus match |
| Geneformer | training_data_overlap | zero_shot_embedding | edited | corpus match |
| Geneformer | training_data_overlap | perturbation_genetic:in_silico_treatment | edited | corpus match |
| UCE | training_data_overlap | zero_shot_embedding:mouse_brain | edited | corpus match |
| UCE | training_data_overlap | annotation:classifier_transfer | edited | corpus match |
| scFoundation | training_data_overlap | zero_shot_embedding | edited | corpus match |
| scFoundation | training_data_overlap | annotation | edited | corpus match |
| scFoundation | training_data_overlap | gene_programs | edited | corpus match |
| TranscriptFormer | training_data_overlap | reference_mapping:spermatogenesis | edited | corpus match |
| TranscriptFormer | training_data_overlap | reference_mapping:lps_state | edited | corpus match |
| CellOT | fair_test_number | perturbation_chemical:4i | edited | [V] resolved |
| CellOT | fair_test_number | perturbation_chemical:sciplex3 | edited | [V] resolved |
| CellOT | run_to_run_spread | all | edited | [V] resolved |
| CPA | run_to_run_spread | all | edited | [V] resolved |
| CPA | availability_corpus | all | edited | [V] resolved |
| CPA | simple_baseline | perturbation_signaling | register note | Field standard (register): no register entry. |
| CPA | simple_baseline | perturbation_chemical:single_drug | register note | Field standard (register): no register entry. |
| CPA | simple_baseline | perturbation_chemical:combinations | register note | Field standard (register): no register entry. |
| CPA | simple_baseline | perturbation_chemical:unseen_drugs | register note | Field standard (register): no register entry. |
| CPA | simple_baseline | perturbation_genetic:combinations | register note | Field standard (register): no register entry for its date (first public bioRxiv Apr 2021; the entry for this task starts later). |
| CPA | simple_baseline | other:perturbation_embedding_clustering | register note | Field standard (register): no register entry. |
| CellFM | simple_baseline | gene_level | register note | Field standard (register): no register entry. |
| CellFM | simple_baseline | perturbation_genetic | register note | Field standard (register): no register entry for its date (first public bioRxiv Jun 2024; the entry for this task starts later). |
| CellFM | simple_baseline | reverse_perturbation | register note | Field standard (register): no register entry. |
| CellFM | simple_baseline | perturbation_chemical | register note | Field standard (register): no register entry. |
| CellFM | simple_baseline | annotation | register note | Field standard (register: SVM or logistic regression on expression (Abdelaal et al., May 2019)): yes (SVM). |
| CellFM | simple_baseline | integration | register note | Field standard (register: unintegrated HVG/PCA reference and Harmony (Luecken et al., May 2020)): no. |
| CellFM | simple_baseline | gene_programs | register note | Field standard (register): no register entry. |
| CellOT | simple_baseline | perturbation_chemical:4i | register note | Field standard (register): no register entry. |
| CellOT | simple_baseline | perturbation_chemical:sciplex3 | register note | Field standard (register): no register entry. |
| CellOT | simple_baseline | perturbation_signaling:lupus_ifnb | register note | Field standard (register): no register entry. |
| CellOT | simple_baseline | perturbation_chemical:glioblastoma | register note | Field standard (register): no register entry. |
| CellOT | simple_baseline | perturbation_signaling:cross_species_lps | register note | Field standard (register): no register entry. |
| CellOT | simple_baseline | other:hematopoiesis_development | register note | Field standard (register): no register entry. |
| CellPLM | simple_baseline | zero_shot_embedding | register note | Field standard (register): no register entry for its date (first public bioRxiv 3 Oct 2023; the entry for this task starts later). |
| CellPLM | simple_baseline | denoising | register note | Field standard (register): no register entry. |
| CellPLM | simple_baseline | denoising:spatial_imputation | register note | Field standard (register): no register entry. |
| CellPLM | simple_baseline | annotation | register note | Field standard (register: SVM or logistic regression on expression (Abdelaal et al., May 2019)): yes (CellTypist, logistic regression). |
| CellPLM | simple_baseline | perturbation_genetic | register note | Field standard (register): no register entry for its date (first public bioRxiv 3 Oct 2023; the entry for this task starts later). |
| GEARS | simple_baseline | perturbation_genetic:single | register note | Field standard (register): no register entry for its date (first public bioRxiv Jul 2022; the entry for this task starts later). |
| GEARS | simple_baseline | perturbation_genetic:combinations | register note | Field standard (register): no register entry for its date (first public bioRxiv Jul 2022; the entry for this task starts later). |
| GEARS | simple_baseline | perturbation_genetic:gi_subtypes | register note | Field standard (register): no register entry for its date (first public bioRxiv Jul 2022; the entry for this task starts later). |
| GEARS | simple_baseline | perturbation_genetic:nonadditive_genes | register note | Field standard (register): no register entry for its date (first public bioRxiv Jul 2022; the entry for this task starts later). |
| GEARS | simple_baseline | perturbation_genetic:cluster_recovery | register note | Field standard (register): no register entry for its date (first public bioRxiv Jul 2022; the entry for this task starts later). |
| GEARS | simple_baseline | other:cell_fitness | register note | Field standard (register): no register entry. |
| Geneformer | simple_baseline | gene_level:dosage_sensitivity | register note | Field standard (register): no register entry. |
| Geneformer | simple_baseline | gene_level:dosage_collins | register note | Field standard (register): no register entry. |
| Geneformer | simple_baseline | gene_level:in_silico_deletion_disease_genes | register note | Field standard (register): no register entry. |
| Geneformer | simple_baseline | gene_level:bivalency | register note | Field standard (register): no register entry. |
| Geneformer | simple_baseline | gene_level:tf_regulatory_range | register note | Field standard (register): no register entry. |
| Geneformer | simple_baseline | gene_level:n1_centrality | register note | Field standard (register): no register entry. |
| Geneformer | simple_baseline | gene_level:n1_targets | register note | Field standard (register): no register entry. |
| Geneformer | simple_baseline | gene_programs:in_silico_deletion_targets | register note | Field standard (register): no register entry. |
| Geneformer | simple_baseline | annotation | register note | Field standard (register: SVM or logistic regression on expression (Abdelaal et al., May 2019)): no (CaSTLe, a boosted-tree classifier, was run; not SVM or logistic regression). |
| Geneformer | simple_baseline | annotation:cross_platform | register note | Field standard (register: SVM or logistic regression on expression (Abdelaal et al., May 2019)): no. |
| Geneformer | simple_baseline | annotation:cardiomyopathy_state | register note | Field standard (register: SVM or logistic regression on expression (Abdelaal et al., May 2019)): no. |
| Geneformer | simple_baseline | integration | register note | Field standard (register: unintegrated HVG/PCA reference and Harmony (Luecken et al., May 2020)): partly (Harmony and ComBat; no unintegrated HVG/PCA reference reported). |
| Geneformer | simple_baseline | zero_shot_embedding | register note | Field standard (register): no register entry for its date (first public Nature May 2023, no preprint; the entry for this task starts later). |
| Geneformer | simple_baseline | perturbation_genetic:in_silico_treatment | register note | Field standard (register): no register entry for its date (first public Nature May 2023, no preprint; the entry for this task starts later). |
| SCimilarity | simple_baseline | annotation | register note | Field standard (register: SVM or logistic regression on expression (Abdelaal et al., May 2019)): yes (CellTypist, logistic regression). |
| SCimilarity | simple_baseline | annotation:cross_platform | register note | Field standard (register: SVM or logistic regression on expression (Abdelaal et al., May 2019)): no. |
| SCimilarity | simple_baseline | integration | register note | Field standard (register: unintegrated HVG/PCA reference and Harmony (Luecken et al., May 2020)): partly (Harmony; no unintegrated HVG/PCA reference). |
| SCimilarity | simple_baseline | reference_mapping | register note | Field standard (register): no register entry. |
| SCimilarity | simple_baseline | gene_programs | register note | Field standard (register): no register entry. |
| STATE | simple_baseline | perturbation_chemical | register note | Field standard (register): no register entry. |
| STATE | simple_baseline | perturbation_signaling | register note | Field standard (register): no register entry. |
| STATE | simple_baseline | perturbation_genetic | register note | Field standard (register: training mean or no-change, additive model for combinations, linear model (Ahlmann-Eltze et al., Sept 2024)): yes (mean and linear baselines). |
| STATE | simple_baseline | other:zero_shot_context | register note | Field standard (register): no register entry. |
| STATE | simple_baseline | zero_shot_embedding | register note | Field standard (register: HVG and Harmony (Kedzierska et al., Oct 2023)): partly (linear probe on HVG expression; Harmony not applicable to a probe and not run). |
| STATE | simple_baseline | reverse_perturbation | register note | Field standard (register): no register entry. |
| STATE | simple_baseline | drug_response:viability | register note | Field standard (register): no register entry. |
| STATE | simple_baseline | drug_response:combination_synergy | register note | Field standard (register): no register entry. |
| STATE | simple_baseline | gene_programs | register note | Field standard (register): no register entry. |
| STATE | simple_baseline | other:target_deconvolution | register note | Field standard (register): no register entry. |
| STATE | simple_baseline | other:genetic_viability_depmap | register note | Field standard (register): no register entry. |
| UCE | simple_baseline | zero_shot_embedding:tabula_sapiens_v2 | register note | Field standard (register: HVG and Harmony (Kedzierska et al., Oct 2023)): partly (PCA on log-normalised expression; Harmony not run). |
| UCE | simple_baseline | integration:ovary_platform | register note | Field standard (register: unintegrated HVG/PCA reference and Harmony (Luecken et al., May 2020)): partly (PCA reference; Harmony not run). |
| UCE | simple_baseline | zero_shot_embedding:brain_hbca | register note | Field standard (register: HVG and Harmony (Kedzierska et al., Oct 2023)): partly (PCA on 5,000 HVGs; Harmony not run). |
| UCE | simple_baseline | zero_shot_embedding:mouse_brain | register note | Field standard (register: HVG and Harmony (Kedzierska et al., Oct 2023)): no. |
| UCE | simple_baseline | zero_shot_embedding:scgraph | register note | Field standard (register: HVG and Harmony (Kedzierska et al., Oct 2023)): no. |
| UCE | simple_baseline | zero_shot_embedding:ontology_organization | register note | Field standard (register: HVG and Harmony (Kedzierska et al., Oct 2023)): no. |
| UCE | simple_baseline | reference_mapping:ima_alignment | register note | Field standard (register): no register entry. |
| UCE | simple_baseline | annotation:cross_species_label_transfer | register note | Field standard (register: SVM or logistic regression on expression (Abdelaal et al., May 2019)): no (SAMap was run). |
| UCE | simple_baseline | annotation:novel_species_centroids | register note | Field standard (register: SVM or logistic regression on expression (Abdelaal et al., May 2019)): no. |
| UCE | simple_baseline | annotation:classifier_transfer | register note | Field standard (register: SVM or logistic regression on expression (Abdelaal et al., May 2019)): no (chance reference only). |
| X-Cell | simple_baseline | perturbation_genetic:pisces_ipsc_hepg2_200 | register note | Field standard (register: training mean or no-change, additive model for combinations, linear model (Ahlmann-Eltze et al., Sept 2024)): no. |
| X-Cell | simple_baseline | perturbation_genetic:replogle_nadig | register note | Field standard (register: training mean or no-change, additive model for combinations, linear model (Ahlmann-Eltze et al., Sept 2024)): no. |
| X-Cell | simple_baseline | perturbation_signaling:parse_1m | register note | Field standard (register): no register entry. |
| X-Cell | simple_baseline | perturbation_chemical:tahoe_zero_shot | register note | Field standard (register): no register entry. |
| X-Cell | simple_baseline | perturbation_genetic:jurkat_context_transfer | register note | Field standard (register: context mean and transfer of measured responses from other contexts (Virtual Cell Challenge, Dec 2025)): yes (transfer of the measured resting-screen effects). |
| X-Cell | simple_baseline | perturbation_genetic:melanocyte_zero_shot | register note | Field standard (register: context mean and transfer of measured responses from other contexts (Virtual Cell Challenge, Dec 2025)): yes (control mean and mean effect from the training cell types). |
| X-Cell | simple_baseline | perturbation_genetic:primary_tcell_zero_shot | register note | Field standard (register: context mean and transfer of measured responses from other contexts (Virtual Cell Challenge, Dec 2025)): yes (control mean and perturbation mean). |
| scFoundation | simple_baseline | denoising:read_depth_enhancement | register note | Field standard (register): no register entry. |
| scFoundation | simple_baseline | denoising:imputation_clustering | register note | Field standard (register): no register entry. |
| scFoundation | simple_baseline | zero_shot_embedding | register note | Field standard (register): no register entry for its date (first public bioRxiv May 2023; the entry for this task starts later). |
| scFoundation | simple_baseline | integration | register note | Field standard (register: unintegrated HVG/PCA reference and Harmony (Luecken et al., May 2020)): no (PCA+BBKNN was run; no unintegrated reference or Harmony). |
| scFoundation | simple_baseline | drug_response:bulk_ic50 | register note | Field standard (register): no register entry. |
| scFoundation | simple_baseline | drug_response:single_cell | register note | Field standard (register): no register entry. |
| scFoundation | simple_baseline | perturbation_genetic | register note | Field standard (register): no register entry for its date (first public bioRxiv May 2023; the entry for this task starts later). |
| scFoundation | simple_baseline | annotation | register note | Field standard (register: SVM or logistic regression on expression (Abdelaal et al., May 2019)): yes (CellTypist, logistic regression). |
| scFoundation | simple_baseline | gene_programs | register note | Field standard (register): no register entry. |
| scFoundation | simple_baseline | other:masked_value_reconstruction | register note | Field standard (register): no register entry. |
| scGPT | simple_baseline | annotation | register note | Field standard (register: SVM or logistic regression on expression (Abdelaal et al., May 2019)): no. |
| scGPT | simple_baseline | reference_mapping | register note | Field standard (register): no register entry. |
| scGPT | simple_baseline | integration | register note | Field standard (register: unintegrated HVG/PCA reference and Harmony (Luecken et al., May 2020)): partly (Harmony; no unintegrated HVG/PCA reference reported). |
| scGPT | simple_baseline | integration:multiomic | register note | Field standard (register: unintegrated HVG/PCA reference and Harmony (Luecken et al., May 2020)): no (Seurat v4 and scMoMat were run). |
| scGPT | simple_baseline | zero_shot_embedding | register note | Field standard (register): no register entry for its date (first public bioRxiv Apr 2023; the entry for this task starts later). |
| scGPT | simple_baseline | perturbation_genetic | register note | Field standard (register): no register entry for its date (first public bioRxiv Apr 2023; the entry for this task starts later). |
| scGPT | simple_baseline | perturbation_genetic:knocktf_bulk | register note | Field standard (register): no register entry for its date (first public bioRxiv Apr 2023; the entry for this task starts later). |
| scGPT | simple_baseline | reverse_perturbation | register note | Field standard (register): no register entry. |
| scGPT | simple_baseline | gene_programs:embedding | register note | Field standard (register): no register entry. |
| scGPT | simple_baseline | gene_programs:attention_grn | register note | Field standard (register): no register entry. |
| TranscriptFormer | simple_baseline | annotation:ood_species | register note | Field standard (register: SVM or logistic regression on expression (Abdelaal et al., May 2019)): no. |
| TranscriptFormer | simple_baseline | annotation:tabula_sapiens2 | register note | Field standard (register: SVM or logistic regression on expression (Abdelaal et al., May 2019)): no. |
| TranscriptFormer | simple_baseline | annotation:disease_covid | register note | Field standard (register: SVM or logistic regression on expression (Abdelaal et al., May 2019)): no. |
| TranscriptFormer | simple_baseline | annotation:tumor_gbm | register note | Field standard (register: SVM or logistic regression on expression (Abdelaal et al., May 2019)): no. |
| TranscriptFormer | simple_baseline | reference_mapping:spermatogenesis | register note | Field standard (register): no register entry. |
| TranscriptFormer | simple_baseline | reference_mapping:lps_state | register note | Field standard (register): no register entry. |
| TranscriptFormer | simple_baseline | reference_mapping:dlpfc | register note | Field standard (register): no register entry. |
| TranscriptFormer | simple_baseline | other:drug_effect_detection | register note | Field standard (register): no register entry. |
| Scouter | simple_baseline | perturbation_genetic:single | register note | Field standard (register: training mean or no-change, additive model for combinations, linear model (Ahlmann-Eltze et al., Sept 2024)): partly (training mean; no linear model). |
| Scouter | simple_baseline | perturbation_genetic:combinations | register note | Field standard (register: training mean or no-change, additive model for combinations, linear model (Ahlmann-Eltze et al., Sept 2024)): no (no additive model). |
| Scouter | simple_baseline | perturbation_genetic:interaction_types | register note | Field standard (register: training mean or no-change, additive model for combinations, linear model (Ahlmann-Eltze et al., Sept 2024)): no (no additive model). |
| Scouter | simple_baseline | perturbation_genetic:cross_dataset | register note | Field standard (register: training mean or no-change, additive model for combinations, linear model (Ahlmann-Eltze et al., Sept 2024)): partly (no-change reference only; no training mean or linear model). |
