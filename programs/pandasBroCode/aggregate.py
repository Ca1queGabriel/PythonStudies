import pandas as pd

df = pd.read_csv("../../resources/overwatch.csv")

df1 = pd.DataFrame([{"Nome": "Caique", "Altura": 1.77, "Profissão": "Engenheiro Software"},{"Nome": "Matheus", "Altura": 1.77, "Profissão": "Desenvolvedor Junior"},{"Nome": "Duda", "Altura": 1.58, "Profissão": "Desenvolvedor Junior"}], index = ["Pessoa 1", "Pessoa 2", "Pessoa 3"])

# print(df1.mean(numeric_only=True)) #mostra média só das colunas numéricas que é praticamente nenhuma kdjaskjdajk
# print(df1.sum(numeric_only=True)) #mesma coisa pra soma
# print(df1.min(numeric_only=True)) #mesma coisa pra min
# print(df1.max(numeric_only=True)) #Mesma coisa pra max
# print(df1.count()) #ele pode ser elementos nao numericos ent nesse caso ele conta as linhas de cada coluna

#single column

# print(df1["Altura"].mean()) #mostra média só das colunas altura
# print(df1["Altura"].sum()) #mesma coisa pra soma
# print(df1["Altura]"].min()) #mesma coisa pra min
# print(df1["Altura"].max()) #Mesma coisa pra max
# print(df1["Altura"].count()) #ele pode ser elementos nao numericos ent nesse caso ele conta as linhas de cada coluna

#group by

group = df1.groupby("Profissão") #resumidamente, ele vai agrupar e trazer os que tem o mesmo tipo agrupado, ent exemplo: tem 2 desenvolvedor junior com profissão igual, e 1 diferente. Ele vai trazer 2 resultados, 1 da soma dos dois se tu agrupar, e 1 desse outro profissional pq são 2 tipos diferentes, ent 2 resultados diferentes apenas

# print(group["Altura"].mean())
# print(group["Altura"].sum())
# print(group["Altura"].min())
print(group["Altura"].max())
print(group.count())