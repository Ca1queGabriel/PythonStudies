import numpy as np


array1 = np.array([[1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]])
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(array1.shape)
print(array2.shape)
print(array1 * array2) #caso tu não tenha entendido ainda o que está acontecendo, é o equivalente ao "chuveirinho" na matemática, ele tá fazendo 1 * elementos da 1 row do array2,
# depois 2 * elementos do array2 até acabar e o array virar um 10x10.