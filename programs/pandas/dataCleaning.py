import pandas as pd

df = pd.read_csv("../../resources/overwatch.csv")

#dropar colunas indesejadas, nesse caso Hero e ReleaseDate
# df = df.drop(columns=["Role", "ReleaseDate"])


# lida com dados faltantes
# df = df.dropna(subset=["Role"]) #remove linhas onde a coluna Role é NaN

# df = df.fillna({"Role": "Unknown"}) #esse tem que ser um dicionário {} -> dicionário [] -> lista, nesse caso ele vai preencher a coluna Role com Unknown onde tiver NaN
#
# print(df.to_string()) #aliás, o to_string() é só pra printar tudo, pq se não ele corta e mostra só uma parte do dataframe

# arrumar valores inconsistentes

df["Role"] = df["Role"].replace({"Support": "Healer",
                                 "Damage": "DPS",
                                 "Tank": "Muralha da China"}) #esse replace é pra substituir valores, nesse caso ele vai substituir Support por Healer, Damage por DPS e Tank por Muralha da China

# df["Role"] = df["Role"].str.upper()
df["Hero"] = df["Hero"].str.lower()
df = df.sort_values("Role")

#conversão de tipos de dados
# df["ReleaseDate"] = df["ReleaseDate"].astype((bool)) #parse de tipo, lembrando que 1 = True, 0 = False, e NaN = False, nesse caso ele vai transformar a coluna ReleaseDate em booleano, onde se tiver algum valor (não NaN) vai ser True, e se for NaN vai ser False
# print(df.to_string())


#alguns testes, mas comparação de data, aliás, se tu deixar


try:
    df["ReleaseDate"] = pd.to_datetime(df["ReleaseDate"], errors="coerce") #esse errors="coerce" é pra transformar os valores inválidos em NaT (Not a Time), que é o equivalente a NaN, mas pra datas
    print(df[df["ReleaseDate"] < pd.to_datetime("2018-01-01")])
except ValueError as e:
    print(f"Puts, deu erro em {e}")



#Playground de py

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Nome deve ser string")
        self._name = value

    @name.getter
    def name(self):
        return str.title(self._name)





class Cachorro:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @nome.getter
    def nome(self):
        return self._nome

    def latir(self):
        print(f"Au au {self.nome} latiu")

