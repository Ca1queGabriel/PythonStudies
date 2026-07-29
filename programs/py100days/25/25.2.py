import pandas as pd

def convertCelsiusToFahreinheit(celsius):
    return celsius * 9/5 + 32

# print(df[df["temp"] == df["temp"].max()])
# print(df["temp"].mean())
df = pd.read_csv("../../../resources/weather_data.csv")
monday_temp = df[df["day"] == "Monday"]["temp"]
f_temp = convertCelsiusToFahreinheit(monday_temp)

data_dict = {
    "Pessoas": ["Caique", "Matheus", "Duda"],
    "Idade": [22, 20, 23],
    "Profissão": ["Programador", "Estudante", "Estudante"]
}

data = pd.DataFrame(data_dict)
data.to_csv("../../resources/amigos.csv", index=False)
data.to_json("../../resources/amigos.json", orient="records")





