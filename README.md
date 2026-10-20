# ab-experiment-copilot

End-to-end Product Funnel & A/B Experimentation readout pipeline combining SQL telemetry extraction, Sample Ratio Mismatch (SRM) validation, frequentist hypothesis testing (`SciPy`), and automated **Ship / Hold / Kill** decision memos.

## Why It Matters
Many product teams ship features based on noisy point estimates without checking for Sample Ratio Mismatch (SRM) or guardrail metric degradation (e.g., refund rate or p95 latency). `ab-experiment-copilot` enforces statistical guardrails first, then generates an executive-ready readout memo.

## Statistical Checks Included
1. **Sample Ratio Mismatch (`chi2_contingency`)**: Flags traffic bucketing bugs if `p < 0.001`.
2. **Conversion Uplift (`two_proportion_z_test`)**: Computes two-sided p-value, 95% confidence interval, and minimum detectable effect (MDE) power check.
3. **Automated Decision Rule**: Outputs `SHIP`, `ITERATE / EXTEND`, or `ROLLBACK` based on primary conversion uplift and guardrail thresholds.
