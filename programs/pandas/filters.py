import pandas as pd


df = pd.read_csv("../../resources/overwatch.csv")

#filtering = Keeping the rows that match a condition

#filtered by role, gathering all tanks
tankOrDamage = df[(df["Role"] == "Tank") | (df["Role"] == "Damage")]

supportAndAna = df[(df["Role"] == "Support") & (df["Hero"] == "Ana")]

print(supportAndAna)