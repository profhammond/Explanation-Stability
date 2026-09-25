# Release Checklist

- [ ] Replace every bracketed placeholder.
- [ ] Add the final manuscript title, author list, venue, year, DOI, and repository URL to `CITATION.cff`.
- [ ] Choose and add an explicit code license.
- [ ] Confirm redistribution permissions for every uploaded file.
- [ ] Remove source images and masks unless redistribution is explicitly permitted.
- [ ] Remove local paths, credentials, access tokens, signed URLs, and private metadata.
- [ ] Add exact model provenance and checksum or document why the model cannot be redistributed.
- [ ] Add the validated cohort and comparison manifests.
- [ ] Add completion statuses for the primary analysis, negative controls, PH2 replication, and protocol-sensitivity audit.
- [ ] Add manuscript-ready derived tables and figures.
- [ ] Confirm all released `.csv.gz` files are genuinely gzip-compressed.
- [ ] Run `python src/verify_release.py --root .` successfully.
- [ ] Compare every manuscript number with the tagged release.
- [ ] Confirm `clinical_validation_claim_authorized` remains `false` wherever applicable.
- [ ] Create an immutable Git tag.
- [ ] Archive the tag and insert its DOI into the manuscript.

