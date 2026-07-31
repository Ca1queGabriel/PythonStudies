import pandas as pd


data = pd.read_csv("../../../../resources/Squirrel_data.csv")

df = data.groupby("Primary Fur Color").size().reset_index(name="Count")



df = df.rename(columns={"Primary Fur Color": "Fur Color"})

df.to_csv("../../../resources/squirrel_count.csv",index= False)

print(df)

for _ in range(0, 10, 2):
    print(_)