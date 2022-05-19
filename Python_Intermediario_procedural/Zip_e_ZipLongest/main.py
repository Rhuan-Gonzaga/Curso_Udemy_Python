"""
Zip - Unido iteraveis
Zip_longest - itertools

"""
from itertools import zip_longest
cidades = ["São Paulo", "Belo Horizonte", "Salvador", "Monte Belo", "Rio de Janiero"]

estados = ["SP", "MG", "BA"]

#Função zip junta as minhas duas listas, confome o tamanho da menor lista
#cidade_estados = zip(estados, cidades)

#Função zip_longest pega todo os valores
cidade_estados = zip_longest(estados, cidades, fillvalue="Estado")

print(list(cidade_estados))