from importlib import resources

import pandas as pd

df = pd.read_csv("../../../resources/overwatch.csv")
# print(df.to_string())


df1 = pd.read_json("../resources/overwatch.json")
print(df1.to_string())