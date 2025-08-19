import numpy as np
import pandas as pd

def generate_ab_data(n_total=5000, p_A=0.10, p_B=0.125, seed=42):
    """
    Generate a synthetic A/B dataset with binary conversion.
    Returns a pandas DataFrame with columns: user_id, group, converted
    """
    rng = np.random.default_rng(seed)
    groups = rng.choice(['A', 'B'], size=n_total, p=[0.5, 0.5])
    converted = np.where(groups == 'A',
                         rng.binomial(1, p_A, size=n_total),
                         rng.binomial(1, p_B, size=n_total))
    df = pd.DataFrame({
        'user_id': np.arange(1, n_total + 1, dtype=int),
        'group': groups,
        'converted': converted
    })
    return df

if __name__ == "__main__":
    df = generate_ab_data()
    out_path = "../data/ab_test_data.csv"
    df.to_csv(out_path, index=False)
    print(f"Saved synthetic data to {out_path}")
