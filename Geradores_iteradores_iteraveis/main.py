"""
ITERADORES E ITERAVEIS

"""

#verificando se uma lista é iteravel (numeros não iteraveis)
#lista2 = "string"
#print(hasattr(lista,'__iter__'))

#lista = [0,1,2,3,4,5]


#Verificando se minha lista é um iterador
#print(hasattr(lista,"__next__"))
#FALSE

#transformando minha lista em um iterador
#lista = iter(lista)
#print(hasattr(lista,"__next__"))
#TRUE

"""

GERADORES

"""
import sys
import time

#Criando um gerador
def gerador():
    for n in range(100):
        yield n
        #time.sleep(0.1)

g = gerador()

for v in g:
    print(v)


#Gerador sem o for
def gera():
    variavel = "Valor 1"
    yield variavel
    variavel = "Valor 2"
    yield variavel
    variavel = "Valor 3"
    yield variavel


g = gera()
#print(next(g))
#print(next(g))
#print(next(g))

#Tamanho de bytes
l1 = [x for x in range(1000)]  #Lista
print(sys.getsizeof(l1))
l2 = (x for x in range(1000)) #Gerador
print(sys.getsizeof(l2))
