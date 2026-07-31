import numpy as np

array = np.array([[1, 2, 3 ,4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# array[start:end:step, start:end:step] <-- o primeiro é para as linhas, o segundo é para as colunas
print(array[0:3:1, 0:2:1]) #vai pegar as primeiras 3 linhas e as primeiras 2 colunas de cada uma