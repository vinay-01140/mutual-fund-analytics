import pandas as pd
import os

folder = "data/raw"

files = [f for f in os.listdir(folder) if f.endswith(".csv")]

print("Total CSV Files:", len(files))

for file in files:
    print("\n" + "=" * 60)
    print("Dataset:", file)

    path = os.path.join(folder, file)

    df = pd.read_csv(path)

    print("Shape:", df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())