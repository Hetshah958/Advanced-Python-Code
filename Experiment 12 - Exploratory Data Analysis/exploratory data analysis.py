from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

def load_data() -> pd.DataFrame:
    """Load customer_churn.csv if supplied; otherwise use a clearly labelled demo dataset."""
    path = Path(__file__).with_name("customer_churn.csv")
    if path.exists():
        print(f"Loading dataset: {path.name}")
        return pd.read_csv(path)

    print("customer_churn.csv not found; using illustrative sample data.")
    return pd.DataFrame({
        "CustomerID": range(1, 16),
        "Age": [24, 27, 22, 32, 29, 25, 100, 41, 36, 28, 31, 45, 26, 39, 33],
        "MonthlyCharges": [50, 60, 52, 58, 62, 55, 600, 75, 68, 49, 80, 95, 54, 72, 65],
        "Tenure": [2, 12, 5, 24, 18, 7, 1, 36, 30, 4, 20, 48, 9, 27, 15],
        "Churn": ["Yes", "No", "No", "No", "Yes", "No", "Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No"],
    })

def main():
    df = load_data()
    print("\nFirst five rows:\n", df.head())
    print("\nDataset information:")
    df.info()
    print("\nDescriptive statistics:\n", df.describe(include="all"))

    numeric = df.select_dtypes(include=np.number)
    if not numeric.empty:
        print("\nMean:\n", numeric.mean())
        print("\nMedian:\n", numeric.median())
        print("\nMode:\n", numeric.mode().head(1))
        print("\nStandard deviation:\n", numeric.std())
        print("\nVariance:\n", numeric.var())
        print("\nMinimum:\n", numeric.min())
        print("\nMaximum:\n", numeric.max())
        print("\nQuantiles:\n", numeric.quantile([0.25, 0.5, 0.75]))

        for column in numeric.columns:
            plt.figure()
            values = df[column].dropna()
            plt.hist(values, bins=10, edgecolor="black")
            plt.title(f"Distribution of {column}")
            plt.tight_layout()
            plt.savefig(f"{column.lower()} histogram.png")
            plt.close()

            plt.figure()
            plt.boxplot(df[column].dropna())
            plt.title(f"Box plot of {column}")
            plt.tight_layout()
            plt.savefig(f"{column.lower()} boxplot.png")
            plt.close()

        if len(numeric.columns) >= 2:
            plt.figure()
            plt.scatter(df[numeric.columns[0]], df[numeric.columns[1]])
            plt.xlabel(numeric.columns[0])
            plt.ylabel(numeric.columns[1])
            plt.title(f"{numeric.columns[0]} vs {numeric.columns[1]}")
            plt.tight_layout()
            plt.savefig("scatter plot.png")
            plt.close()

            plt.figure()
            correlation = numeric.corr()
            plt.imshow(correlation, interpolation="nearest", vmin=-1, vmax=1)
            plt.colorbar()
            plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45, ha="right")
            plt.yticks(range(len(correlation.columns)), correlation.columns)
            for row in range(len(correlation.columns)):
                for col in range(len(correlation.columns)):
                    plt.text(col, row, f"{correlation.iloc[row, col]:.2f}", ha="center", va="center")
            plt.title("Correlation Matrix")
            plt.tight_layout()
            plt.savefig("correlation heatmap.png")
            plt.close()

    print("\nMissing values before cleaning:\n", df.isna().sum())
    cleaned = df.copy()
    for column in cleaned.columns:
        if pd.api.types.is_numeric_dtype(cleaned[column]):
            cleaned[column] = cleaned[column].fillna(cleaned[column].median())
        else:
            mode = cleaned[column].mode()
            if not mode.empty:
                cleaned[column] = cleaned[column].fillna(mode.iloc[0])

    numeric_clean = cleaned.select_dtypes(include=np.number)
    if not numeric_clean.empty:
        scores = numeric_clean.apply(lambda col: zscore(col, nan_policy="omit") if col.nunique() > 1 else 0)
        outlier_mask = (scores.abs() > 3).any(axis=1)
        print("\nPotential outlier rows (absolute z-score > 3):\n", cleaned[outlier_mask])
        # Cap numeric columns at mean +/- 3 standard deviations.
        for column in numeric_clean.columns:
            mean, std = cleaned[column].mean(), cleaned[column].std()
            if pd.notna(std) and std > 0:
                cleaned[column] = cleaned[column].clip(mean - 3 * std, mean + 3 * std)

    output = Path(__file__).with_name("cleaned customer churn.csv")
    cleaned.to_csv(output, index=False)
    print("\nMissing values after cleaning:\n", cleaned.isna().sum())
    print(f"Cleaned data saved to: {output.name}")

if __name__ == "__main__":
    main()
