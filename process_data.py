import pandas as pd
import glob

# Load all csv files
files = glob.glob("data/*.csv")
print("Files found:", files)


df_list = [pd.read_csv(file) for file in files]
df = pd.concat(df_list, ignore_index=True)

# Filter Pink Morsels
df = df[df["product"].str.lower() == "pink morsel"]

# Clean price column
df["price"] = df["price"].replace(r'[\$,]', '', regex=True).astype(float)

# Create sales column
df["sales"] = df["quantity"] * df["price"]

df = df[["sales", "date", "region"]]

df.to_csv("output.csv", index=False)

print("Processing complete!")