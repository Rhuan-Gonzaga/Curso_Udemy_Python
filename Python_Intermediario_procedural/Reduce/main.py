from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10]

soma_lista = reduce(lambda ac, v: ac + v, 0, lista)
print(soma_lista)