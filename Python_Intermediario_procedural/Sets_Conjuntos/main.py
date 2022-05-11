"""
SET / CONJUNTOS
DIFERENTE DE DIC, ELE NÃO TEM CHAVE E 
NÃO RESPEITAM A ORDEM
NÃO ACEITA ELEMENOTS DUPLICADOS
"""

#s1 = {1,2,3,4,5}
#print(s1)

s1 = set()
#Add um valor a set
s1.add(1)
s1.add(2)
s1.add(3)
print(s1)

#Remove um valor de set
s1.discard(2)
print(s1)

#Update separa meu valor e itera 
s1.update("Python")
print(s1)

#Union ou | Une os meus conjuntos
s2 = {3,4,5,6}
s3 = {3,8,9,10}
s4 = s2 | s3
print(s4)

#Une todos os elementos presentos nos dois sets
s2 = {3,4,5,6}
s3 = {3,8,9,10}
s4 = s2 & s3
print(s4)

#difference - Pega o elemento no set da esquerda
s2 = {3,4,5,6}
s3 = {3,4,9,10}
s4 = s3 - s2
print(s4)

#symetric_difference ^ elementos que estão nos dois sets, mas não em ambos
s2 = {3,4,5,6}
s3 = {3,4,9,10}
s4 = s3 ^ s2
print(s4)