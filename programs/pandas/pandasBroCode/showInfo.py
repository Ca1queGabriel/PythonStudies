import pandas as pd

df = pd.read_csv("../../../resources/overwatch.csv")

# print(df.head(10))

# print(df.info())

print(df.describe())
