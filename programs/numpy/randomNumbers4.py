import numpy as np

rng = np.random.default_rng()

fruits = np.array(["apple", "banana", "cherry", "coconut", "pineapple"])

fruit = rng.choice(fruits, size=(3,3)) #ele vai escolher elementos aleatórios pra uma lista de 3 elementos, 1 row, 3 colunas. Podem repetir(é aleatório mesmo, lol)
print(fruit)