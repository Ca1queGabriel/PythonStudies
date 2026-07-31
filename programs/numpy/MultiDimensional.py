import numpy as np


# Não ironicamente é minha primeira matriz multidimensional.. isso aí é 3x3x4. Melhor maneira de pensar nisso é em um cubo mágico
array = np.array([[['A', 'B', 'C', 'D'],['E', 'F', 'G', 'H'],['I', 'J', 'K', 'L']],
                  [['M', 'N', 'O', 'P'],['Q', 'R', 'S', 'T'],['U', 'V', 'W', 'X']],
                  [['Y', 'Z', '1', '2'],['3', '4', '5', '6'],['7', '8', '9', '0']]])

print(array.shape)  # Output: (3, 3, 4)

print(array[0,1,1])  # Output: F

word = array[0,0,0] + array[1,1,1] + array[1,1,1] + array[1,0,2] + array[2,0,1] #Output: arroz

print(word)