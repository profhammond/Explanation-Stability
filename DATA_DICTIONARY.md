# Data Dictionary

The final release may contain a subset of these tables. Column names should remain stable after the first archival release.

## Common identifiers

| Column | Meaning |
|---|---|
| `image_id` | Dataset image identifier used as the highest available resampling unit. |
| `condition` | `baseline`, `dullrazor`, `telea`, or `navier_stokes`. |
| `attribution_method` | `gradcam`, `gradcampp`, or `eigencam`. |
| `evaluation_id` | Unique condition-method-image evaluation identifier. |
| `comparison_id` | Unique baseline-to-condition paired-comparison identifier. |

## Explanation stability

| Column | Meaning |
|---|---|
| `pearson_corr` | Pearson correlation between paired attribution maps. |
| `ssim` | Structural similarity between paired attribution maps. |
| `corr_drift` | Correlation drift, `1 - (pearson_corr + 1) / 2`. |
| `structural_drift` | Structural drift, `1 - ssim`. |
| `edi_primary` | Primary EDI, `(corr_drift + structural_drift) / 2`. Lower values indicate greater paired-map stability. |

## Faithfulness

| Column | Meaning |
|---|---|
| `substrate` | Pixel-replacement substrate used in the perturbation protocol. |
| `steps` | Number of deletion or insertion steps. |
| `deletion_auc` | Area under the deletion probability curve; lower is interpreted as stronger measured deletion faithfulness. |
| `insertion_auc` | Area under the insertion probability curve; higher is interpreted as stronger measured insertion faithfulness. |
| `deletion_confidence_drop` | Change from unperturbed probability to the terminal deletion probability. |
| `deterioration_deletion_auc` | Condition deletion AUC minus baseline deletion AUC; positive values indicate deterioration. |

## Localization

| Column | Meaning |
|---|---|
| `energy_inside_lesion` | Fraction of attribution energy inside the expert lesion mask. |
| `pointing_hit` | Indicator that the attribution maximum lies inside the lesion. |
| `soft_iou` | Continuous attribution-mask intersection over union. |
| `topk_iou` | IoU after thresholding the attribution map at the specified top-k fraction. |
| `deterioration_soft_iou` | Baseline soft IoU minus condition soft IoU; positive values indicate deterioration. |

## Inference summaries

| Column | Meaning |
|---|---|
| `spearman_rho` | Spearman association between EDI and the specified deterioration outcome. |
| `ci_low`, `ci_high` | Image-clustered bootstrap confidence limits. |
| `valid_bootstraps` | Number of valid bootstrap replications. |
| `bootstrap_p` | Bootstrap-based two-sided probability measure used by the audit. |
| `bh_q` | Benjamini-Hochberg adjusted value within the prespecified test family. |
| `multiplicity_resistant` | Whether the result met the prespecified multiplicity-adjusted criterion. |

## Status and authorization fields

| Field | Meaning |
|---|---|
| `run_complete` | All expected computational tasks and outputs were found. |
| `validation_passed` | Prespecified numerical and provenance gates passed. |
| `protocol_sensitivity_claim_authorized` | The protocol-sensitivity conclusion may be reported. |
| `external_localization_replication_claim_authorized` | The PH2 result may be described as an external localization replication. |
| `clinical_validation_claim_authorized` | Whether clinical validation may be claimed. This is expected to remain `false`. |

