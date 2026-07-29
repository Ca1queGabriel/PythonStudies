import pandas as pd

#Series

serie = {"Caique": 100, "Matheus": 200, "Duda": 300 }

series = pd.Series(serie)

# print(series[series > 200])

#DataFrames

dataframe = {
    "Nome": ["Caique", "Matheus", "Duda"],
    "Dinheiro": [100, 200, 300]
}

dataFrames = pd.DataFrame(dataframe, index=["Pessoa 1", "Pessoa 2", "Pessoa 3"])

# Col nova no DataFrame

dataFrames["Idade"] = [21, 20, 23]

# Row nova no DataFrame

new_row = pd.DataFrame([{"Nome": "Amef", "Dinheiro": 50, "Idade": 20}], index=["Pessoa 4"])
dataFrames = pd.concat([dataFrames, new_row])
print(dataFrames)

