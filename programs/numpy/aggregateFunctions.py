import numpy as np

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

print(np.sum(array)) # 55 vai somar tudo
print(np.mean(array)) # 5.5 é a média
print(np.std(array)) # coisa de estatística...
print(np.var(array)) # variação
print(np.min(array)) #min <- entrega o valor que é 1
print(np.max(array)) #max <- entrega o valor, que é 10
print(np.argmin(array)) #min <- entrega a POSIÇÃO, que é 0
print(np.argmax(array)) #max <- entrega a POISÇÃO, que é 9. Sim.. é linear, não [1][4]

print(np.sum(array, axis=0)) #esse argumento é bem interessante, ele resumidamente fala pra tu somar as colunas, ent é 1 + 6, 2 + 7.. etc.
print(np.sum(array, axis=1)) #aqui ele faz com as rows