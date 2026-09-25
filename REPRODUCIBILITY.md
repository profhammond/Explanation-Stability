# Reproducibility Guide

## Environment

The original analyses were executed in Python with TensorFlow/Keras, NumPy, pandas, SciPy, scikit-image, scikit-learn, OpenCV, and Matplotlib. Record exact package versions in the archival release by exporting the validated runtime rather than relying only on unconstrained minimum versions.

## Required external assets

Full computational reproduction requires:

1. ISIC images and lesion masks obtained from the official archive;
2. PH2 images and expert lesion masks obtained from the official provider;
3. the frozen EfficientNet-B0 model or a documented procedure for resolving it;
4. the released cohort manifest and file checksums; and
5. sufficient compute for attribution generation and image-clustered bootstrap inference.

## Recommended execution order

1. Resolve source images and masks without copying them into this repository.
2. Verify identifiers and checksums against the released manifests.
3. Verify the frozen model checksum and positive-melanoma target convention.
4. Reproduce deterministic preprocessing inputs.
5. Generate Grad-CAM, Grad-CAM++, and Eigen-CAM maps with row-level diagnostics.
6. Compute EDI and its two components.
7. Compute deletion/insertion and lesion-localization outcomes.
8. Construct paired deterioration outcomes relative to baseline.
9. Run image-clustered bootstrap inference and multiplicity correction.
10. Execute negative controls and protocol-sensitivity analyses.
11. Run `src/verify_release.py` before interpreting or publishing results.

## Numerical reproduction boundary

The protocol-sensitivity audit achieved practical rather than exact probability parity with the earlier evaluation: maximum absolute error 0.0122, mean absolute error 0.0014, rank agreement 0.99995, and 399/400 agreement at the 0.5 classification threshold. The sole disagreement occurred immediately around the threshold. The release therefore authorizes practical robustness of the conclusion, not bitwise or exact probability reproduction.

## Resampling unit

The source image is the highest available clustering unit. Reliable patient identifiers were unavailable for the analyzed cohorts. Confidence intervals are therefore image-clustered and must not be described as patient-clustered.

