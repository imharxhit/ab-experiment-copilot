#!/usr/bin/env python3
"""Automated A/B Experiment Statistical Validator & Decision Memo Generator."""
import json
import math


def normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def evaluate_ab_test(exp_id: str, n_ctrl: int, conv_ctrl: int, n_treat: int, conv_treat: int) -> dict:
    total_n = n_ctrl + n_treat
    p1, p2 = conv_ctrl / n_ctrl, conv_treat / n_treat
    p_pool = (conv_ctrl + conv_treat) / total_n
    se_pool = math.sqrt(p_pool * (1.0 - p_pool) * (1.0 / n_ctrl + 1.0 / n_treat))
    z = (p2 - p1) / se_pool
    p_val = 2.0 * (1.0 - normal_cdf(abs(z)))
    rel_uplift = ((p2 - p1) / p1) * 100.0
    rec = "SHIP_TO_100_PCT" if (p_val < 0.05 and p2 > p1) else "HOLD_INSUFFICIENT_EVIDENCE"
    return {
        "experiment_id": exp_id,
        "control_conv_pct": round(p1 * 100, 2),
        "treatment_conv_pct": round(p2 * 100, 2),
        "relative_uplift_pct": round(rel_uplift, 2),
        "z_stat": round(z, 3),
        "p_value": round(p_val, 5),
        "recommendation": rec,
    }


if __name__ == "__main__":
    print(json.dumps(evaluate_ab_test("EXP-CHECKOUT-ONECLICK-2026", 48210, 2121, 48390, 2342), indent=2))
