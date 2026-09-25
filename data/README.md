# Data Directory

Do not commit licensed source images or masks here by default.

Recommended public contents:

```text
data/
  manifests/
    isic100_cohort.csv
    ph2_cohort.csv
  checksums/
    source_file_checksums.csv
  derived/
    primary_paired_comparisons.csv.gz
    ph2_paired_comparisons.csv.gz
    negative_control_summary.csv
    perturbation_protocol_results.csv.gz
```

Each manifest should contain only the identifiers and metadata necessary to reconstruct and audit the analytic cohort. Replace private absolute paths with repository-relative or user-configured paths before release.

