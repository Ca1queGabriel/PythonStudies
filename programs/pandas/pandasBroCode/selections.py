import pandas as pd


df = pd.read_csv("../../../resources/overwatch.csv", index_col="Hero")
#OU
df1 = pd.read_json("../resources/overwatch.json").set_index("hero")

# selection by column
# print(df["hero"].to_string())
# print(df["role"].to_string())
# print(df[["hero", "role"]].to_string())

# filtered selection
# print(df[df["role"] == "Tank"])

# selection by row
# print(df1.loc["Ana":"Echo", ["role", "releaseDate"]]) #esse : no meio de Ana e Echo funciona como um inBetween dos dois
# print(df1.iloc[0:11:2, 0:2]) #vai pegar da primeira linha até a 11° (12 elementos) e trazer de 2 em 2 (não vai trazer 12 no total, só 6. Depois do, eu coloquei limitação de coluna, ent ele trás as primeiras 2 colunas


heroi = input("Enter hero name: ")
heroi = heroi.title() # caique -> Caique; Anna -> Anna

#boa chance de aprender o exception do python, lol
try:
    print(df1.loc[heroi])
except KeyError:
    print(f"Hero {heroi} not found")