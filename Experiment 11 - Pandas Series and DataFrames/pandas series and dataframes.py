import numpy as np
import pandas as pd

# Create a Series containing ten random numbers (reproducible output).
rng = np.random.default_rng(seed=42)
series = pd.Series(rng.integers(1, 100, size=10), name="Random Numbers")
print("Pandas Series with ten random numbers:")
print(series)
print("\nSeries summary:")
print(series.describe())

# Create and inspect a DataFrame.
students = pd.DataFrame({
    "Name": ["Aarav", "Diya", "Kabir", "Mira", "Mira"],
    "Age": [20, 21, np.nan, 22, 22],
    "City": ["Pune", "Mumbai", "Delhi", None, None],
    "Score": [85, 91, 78, 88, 88],
})
print("\nOriginal DataFrame:")
print(students)
print("\nSelect columns:")
print(students[["Name", "Score"]])
print("\nFirst two rows using iloc:")
print(students.iloc[:2])
print("\nMissing values:")
print(students.isna().sum())

cleaned = students.copy()
cleaned["Age"] = cleaned["Age"].fillna(cleaned["Age"].mean())
cleaned["City"] = cleaned["City"].fillna("Unknown")
cleaned = cleaned.drop_duplicates()
print("\nCleaned DataFrame:")
print(cleaned)

print("\nMean score by city:")
print(cleaned.groupby("City")["Score"].mean())
