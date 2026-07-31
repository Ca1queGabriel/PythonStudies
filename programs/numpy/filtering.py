import numpy as np

#Filtro

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])


teenagers = ages[ages < 18] #é diferente de um ages(ages < 18) <-- isso é uma expressão booleana, vai retornar false ou true ages[ages < 18] é uma filtragem. Igual em pandas
                            # df[df["age"] < 18]
adults = ages [(ages >= 18) & (ages < 65)] #em numpy n pode ser and, tem que ser &. Bem que podia ser &&
seniors = ages [(ages >= 65) & (ages < 100)]
fossils = ages[ages > 100]

evens = ages[ages%2 == 0]
odds = ages[~ages%2 == 0] #dá pra usar o ~ pra negação, eu prefiro, mas um != também resolvia

print(teenagers)
print(adults)
print(seniors)
print (fossils)
print(evens)
print(odds)