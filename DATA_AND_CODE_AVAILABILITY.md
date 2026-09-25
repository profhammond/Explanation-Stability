# Data and Code Availability

## Suggested manuscript statement

Code, analysis specifications, validation utilities, and non-image derived outputs supporting this study will be released at **[INSERT PUBLIC REPOSITORY URL]** under version **[INSERT TAG OR COMMIT]**. Source dermoscopic images and expert masks are not redistributed; they must be obtained from the ISIC Archive and PH2 under their respective access and licensing terms. The release includes cohort identifiers, provenance records, completion statuses, derived association tables, clustered-bootstrap summaries, and figure-generation inputs sufficient to audit the reported numerical claims. Full regeneration additionally requires the frozen model artifact and locally obtained source images. No patient-level identifiers are included, and the study does not authorize clinical use or a clinical EDI threshold.

## Public-release contents

The final tagged release should contain:

- exact cohort identifiers and image-mask linkage outcomes;
- hashes or checksums for locally resolved source files when redistribution is prohibited;
- frozen-model provenance and checksum, subject to distribution rights;
- preprocessing and attribution specifications;
- EDI component and formula definitions;
- derived faithfulness and localization tables;
- clustered-bootstrap summary tables;
- completion and validation status files;
- scripts that verify release integrity and regenerate tables and figures; and
- a claim-authorization record distinguishing methodological, external-replication, and clinical claims.

## Items that should not be uploaded automatically

- ISIC or PH2 source images and masks without explicit redistribution permission;
- Google Drive paths, access tokens, credentials, or signed URLs;
- model checkpoints whose redistribution terms have not been checked;
- patient identifiers or uncontrolled metadata exports; and
- intermediate caches that are not required to verify a reported result.

## Versioning

Every manuscript submission should cite an immutable Git tag or archival DOI rather than the moving default branch. The release tag should be created only after `src/verify_release.py` passes and the release checklist is signed off.

