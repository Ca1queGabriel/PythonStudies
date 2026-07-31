import numpy as np

#Esse exemplo é bem curto, mas é bem útil, pq é fácil de entender também..
list = np.array([1, 2, 3, 4, 5 ,6, 7, 8, 9, 10])

print(list.shape) # 10, <- 1 elemento, 1 row, 10 colunas
print(list.reshape((2,5))) #resulta em [[1, 2, 3, 4, 5][6, 7, 8, 9, 10]]. Sim, ele vai dividir os elementos.