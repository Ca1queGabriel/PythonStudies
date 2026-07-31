import numpy as np

np.random.seed(seed=1)#essa tag nem é necessária, o valor direto funciona, mas bote por legibilidade.

print(np.random.uniform(low= 0, high = 10, size = (3, 1, 1))) #resumidamente, ele pega os números infinitos tb, ent 0000000312321312,132 etc.. ao invés de só 1, 2, 3 ,4 etc..