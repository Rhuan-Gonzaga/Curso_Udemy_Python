"""
Combinations, permutations e product - itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores unicos
Produto - Ordem importa e repete valores unicos

"""

#from itertools import combinations
#from itertools import permutations
from itertools import product

pessoas = ["Luiz", "André", "Eduardo", "Letícia", "Fabrício", "Rose"]

#for grupo in combinations(pessoas,2):
    #print(grupo)

#for grupo in permutations(pessoas, 2):
    #print(grupo)

for grupo in product(pessoas, repeat= 2):
    print(grupo)