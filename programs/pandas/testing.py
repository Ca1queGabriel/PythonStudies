import pandas as pd

df = pd.read_csv("../../resources/overwatch.csv", index_col="Hero")

# print(df[["Role"]].to_string())

print(df.iloc[:,1].to_string())