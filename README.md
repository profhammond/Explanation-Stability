# Explanation Stability, Faithfulness, and Lesion Localization

This repository supports the manuscript:

> **When Explanation Stability Does Not Imply Explanation Quality: Associations with Faithfulness and Lesion Localization in Dermoscopic Classification**

The study evaluates whether paired attribution-map stability, measured with the Explanation Drift Index (EDI), is associated with deterioration in perturbation faithfulness or lesion-mask localization after deterministic preprocessing. The primary analysis uses a frozen EfficientNet-B0 melanoma classifier, a balanced 100-image ISIC cohort, three attribution methods, and three preprocessing transformations. PH2 provides an auxiliary external localization replication.

## Main findings supported by this release

- In ISIC-100, EDI was not detectably associated with deletion-AUC deterioration or soft-IoU deterioration.
- The deletion-faithfulness conclusion was unchanged across three perturbation substrates and 10, 20, and 50 deletion steps.
- Absolute deletion AUC remained sensitive to the perturbation substrate.
- PH2 produced method-dependent stability-localization associations rather than a universal relationship.
- Negative controls showed metric-dependent behavior and do not establish general clinical validity.

These findings are bounded to the evaluated model, cohorts, attribution methods, preprocessing transformations, metrics, and protocols. The repository does **not** provide a clinically validated EDI threshold or establish explanation correctness.

## Repository layout

```text
config/                 Machine-readable analysis specifications
data/                   Instructions and derived-data schema
evidence/               Validated status files and compact audit outputs
results/                 Manuscript-ready derived tables and figures
src/                     Validation and reproduction utilities
DATA_AND_CODE_AVAILABILITY.md
DATA_DICTIONARY.md
REPRODUCIBILITY.md
CLAIM_BOUNDARIES.md
RELEASE_CHECKLIST.md
CITATION.cff
requirements.txt
```

## Data access

The repository must not redistribute ISIC or PH2 source images unless their governing licenses expressly permit redistribution. Users should obtain source data from the official providers and construct the analytic cohorts using the released identifiers, checksums, and manifests. Derived non-image tables may be released after confirming that they contain no prohibited or identifying information.

See [DATA_AND_CODE_AVAILABILITY.md](DATA_AND_CODE_AVAILABILITY.md) and [data/README.md](data/README.md).

## Reproduction levels

1. **Evidence verification:** verify completion statuses, row counts, key uniqueness, formula identities, and authorized claims from the compact release.
2. **Statistical reproduction:** regenerate manuscript tables and figures from released derived tables.
3. **Full computational reproduction:** regenerate inputs, attribution maps, faithfulness curves, localization metrics, and clustered-bootstrap inference after independently obtaining the source images and model artifact.

The compact public release is intended to support Levels 1 and 2. Level 3 additionally requires licensed datasets and the frozen model artifact.

## Quick validation

```bash
python -m pip install -r requirements.txt
python src/verify_release.py --root .
```

The command fails if a required status is incomplete, a released table is unreadable, duplicate keys are detected where a key specification is supplied, or a manuscript claim exceeds its authorization flag.

## Citation

Use the metadata in `CITATION.cff`. Replace the DOI, venue, repository URL, and release date after archival release.

## License

Add a code license before public release. Dataset licenses and terms remain controlling for all source images and annotations and are not superseded by a repository code license.

