"""
count - Itertools

"""

from itertools import count

contador = count(start=0, step=2)
for valor in contador:
    print(valor)

    if valor >= 10:
        break