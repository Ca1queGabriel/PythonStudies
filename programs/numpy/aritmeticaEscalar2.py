import numpy as np

# Exercise


radii = np.array([1,2,3,4,5]) #raios
print(np.pi * radii ** 2) #área do círculo


array1 = np.array([1, 2 ,3])
array2 = np.array([4, 5 ,6])


#usando dois arrays
print (array1 + array2) # ele soma certinho um com um. Mas lembrando, tem que ter o exato MESMO shape, caso contrário, raiseExcpt.
print (array1 - array2)
print (array1 * array2)
print (array1 / array2)
print (array1 ** array2)

# Operadores de comparação

notas = np.array([91, 55, 100, 73, 82, 64])
print(notas >= 60) #é uma comparação, então o valor retornado vai ser False or True
notas[notas < 60] = 0 #de certa forma o funcionamento usando o numpy é "tipo" um foreach, então é tipo um foreach(nota in notas) {nota = (nota < 60 ? 0 : nota)} <-- C#
print(notas)