import matplotlib.pyplot as plt

def plot_cr_with_ci(summary_df, group_col='group', cr_col='cr', se_col='se', title='A/B Test: Conversion Rate with 95% CI'):
    """
    Simple bar chart with 95% CI error bars.
    """
    z_crit = 1.96
    labels = summary_df[group_col].tolist()
    means = summary_df[cr_col].values
    errors = z_crit * summary_df[se_col].values

    plt.figure(figsize=(6,4))
    plt.bar(labels, means, yerr=errors, capsize=8)
    plt.ylabel('Conversion Rate')
    plt.title(title)
    plt.tight_layout()
    plt.show()
