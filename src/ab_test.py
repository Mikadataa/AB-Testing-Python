from math import erf, sqrt
import pandas as pd

def _norm_cdf(z):
    # Standard normal CDF using erf (no scipy dependency)
    return 0.5 * (1 + erf(z / sqrt(2)))

def propor_z_test(df: pd.DataFrame, group_col='group', outcome_col='converted', control='A', treatment='B'):
    """
    Two-proportion z-test comparing conversion between treatment and control groups.
    Returns a dict with rates, uplift, z, p, and 95% CI for uplift.
    """
    g = df.groupby(group_col)[outcome_col].agg(['sum', 'count']).rename(columns={'sum':'conversions','count':'n'})
    p1 = g.loc[control, 'conversions'] / g.loc[control, 'n']
    p2 = g.loc[treatment, 'conversions'] / g.loc[treatment, 'n']
    n1, n2 = g.loc[control, 'n'], g.loc[treatment, 'n']
    x1, x2 = g.loc[control, 'conversions'], g.loc[treatment, 'conversions']

    # pooled standard error
    p_pool = (x1 + x2) / (n1 + n2)
    se_pool = sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))
    z = (p2 - p1) / se_pool

    # two-sided p-value
    p_val = 2 * (1 - _norm_cdf(abs(z)))

    # 95% CI for (p2 - p1) using unpooled SE
    z_crit = 1.96
    se_diff = sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    diff = p2 - p1
    diff_ci = (diff - z_crit * se_diff, diff + z_crit * se_diff)

    return {
        'p_control': p1, 'p_treatment': p2,
        'n_control': n1, 'n_treatment': n2,
        'uplift': diff,
        'uplift_ci_low': diff_ci[0],
        'uplift_ci_high': diff_ci[1],
        'z': z, 'p_value': p_val
    }

def group_summary(df: pd.DataFrame, group_col='group', outcome_col='converted'):
    """
    Returns per-group N, conversions, conversion rate, and 95% CI.
    """
    z_crit = 1.96
    g = df.groupby(group_col)[outcome_col].agg(['sum','count']).rename(columns={'sum':'conversions','count':'n'}).copy()
    g['cr'] = g['conversions'] / g['n']
    g['se'] = (g['cr'] * (1 - g['cr']) / g['n']) ** 0.5
    g['cr_ci_low'] = g['cr'] - z_crit * g['se']
    g['cr_ci_high'] = g['cr'] + z_crit * g['se']
    return g.reset_index()
