"""
_ protected/private (public _)
__ private 
acessar o valor da classe (_NOMECLASSE__nomeatributo)
"""
from math import prod


class Dados:
    def __init__(self):
        #self.dados = {}
        #self._dados = {}
        self.__dados = {}

    
    def inserir_produtos(self,id,nome):
        #if "produtos" not in self.dados:
        #if "produtos" not in self._dados:
        if "produtos" not in self.__dados:
            #self.dados["produtos"] = {id: nome}
            #self._dados["produtos"] = {id: nome}
            self.__dados["produtos"] = {id: nome}
        else:
            #self.dados["produtos"].update({id: nome})
            #self._dados["produtos"].update({id: nome})
            self.__dados["produtos"].update({id: nome})
    
    def lista_produtos(self):
        #for id, nome in self.dados["produtos"].items():
        #for id, nome in self._dados["produtos"].items():
        for id, nome in self.__dados["produtos"].items():
            print(id, nome)


#Publico
#produto1 = Dados()
#produto1.inserir_produtos(1,"Leite")
#produto1.dados = "Quebrando o codigo"
#produto1.lista_produtos()

#Protegido
#produto2 = Dados()
#produto2.inserir_produtos(2,"Morango")
#produto2._dados = "testando"
#produto2.lista_produtos()

#Privado
produto3 = Dados()
produto3.inserir_produtos(3,"Arroz")
produto3.__dados = "testando"
produto3.lista_produtos()
print(produto3.__dados)
print(produto3._Dados__dados)
