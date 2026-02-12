import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "Data")  # go up one level, then Data folder
csv_path = os.path.join(DATA_DIR, "metabric_RNA.csv")

df = pd.read_csv(csv_path)
print(df.head())