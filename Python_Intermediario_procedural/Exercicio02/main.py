"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retorando uma nova lista com os valores somados:

se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor

Exemplo:
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

===================== Resultado
lista_soma = [2,4,6,8]
"""
list_a =[1,2,3,4,5,6,7]
list_b = [1,2,3,4]

list_c = zip(list_a,list_b)

list_sum = [sum(valor) for valor in list_c]
print(list_sum)