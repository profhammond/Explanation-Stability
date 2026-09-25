# Evidence Imports

Copy only validated, compact outputs into this directory. Every imported run must include a status file with both `run_complete: true` and `validation_passed: true` before its numerical results are used.

Required evidence families for the manuscript:

- primary ISIC-100 faithfulness/localization analysis;
- negative-control audit;
- PH2 external localization replication;
- faithfulness perturbation-protocol sensitivity audit; and
- cross-cohort reconciliation or manuscript-readiness audit.

Keep original run directories immutable. Prefer copying compact derived tables and statuses into a tagged release rather than editing completed experiment outputs in place.

