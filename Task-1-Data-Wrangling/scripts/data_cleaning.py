import pandas as pd

df = pd.read_csv("../data/raw_dataset.csv")

print("Original Dataset")
print(df.head())

print("Rows and Columns:")
print(df.shape)

df = df.drop_duplicates()

df = df.fillna("Unknown")

df.columns = df.columns.str.lower().str.replace(" ", "_")

df.to_csv("../data/cleaned_dataset.csv", index=False)

print("Data Cleaning Completed")