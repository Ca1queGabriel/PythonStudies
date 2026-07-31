import numpy as np

# Filtro sabor LINQ Expression ou filtro de SQL, lol

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])


adults = np.where((ages >= 18) & (ages < 65), ages, "hello") #np.where(condition,array,defaultValue) Aliás, ter botado uma string no default, converteu tudo pra string, aparentemente o comum é 0 ou -1
print(adults)
