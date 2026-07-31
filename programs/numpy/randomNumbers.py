import datetime

import numpy as np

#numeros aleatórios

# tu tem que criar uma seed igual no C++
# also, funciona igual no mine ou terraria, se a seed for igual, os resultados também serão. Então é comum usar a data ou horário do próprio PC no C++, por exemplo, no numpy ele já te dá uma se tu n botar.
# de acordo com pesquisas: "Na prática, ele pede ao SO alguns bytes aleatórios (por exemplo, no Linux de /dev/urandom; no Windows da API criptográfica do sistema). Essa entropia é usada para inicializar o algoritmo interno (PCG64 por padrão)."
rng = np.random.default_rng(seed = 1)

#não, esses index não podem ser qualquer coisa, eu tentei e não são obrigatórios. Mas deixa o código mais legível.
print(rng.integers(low=1, high=7, size=(3, 2, 3)))  #1 > x < 7, e vai retornar 3 elementos com 2 linhas cada e 3 colunas (tudo preenchido com número aleatório) size serve pra isso