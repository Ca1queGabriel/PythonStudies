import numpy as np

array1 = np.array([[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
array2 = np.array([[1, 2, 3, 4],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

#a regra é clara, pra dar um broadcasting, um dos itens na coluna tem que ser 1

print ( array1 * array2)
