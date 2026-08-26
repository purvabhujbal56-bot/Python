import pandas as pd
import numpy as np

data = {
    "Name": ["Purva", "Manaswi", np.nan],
    "Age": [20, np.nan, 22]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Fill missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nCleaned Data:")
print(df)