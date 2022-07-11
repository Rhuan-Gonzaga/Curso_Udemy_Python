
"""
Public, private, protected
_ protected/private (public _)
__ private (_NOMECLASSE__nomeatributo)
"""
class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    
    def inserir_clientes(self,id,nome):
        if "clientes" not in self.__dados:
            self.__dados["clientes"] = {id: nome}
        else:
            self.__dados["clientes"].update({id: nome})
    
    def lista_clientes(self):
        for id, nome in self.__dados["clientes"].items():
            print(id, nome)

bd = BaseDeDados()
bd.inserir_clientes(1,"Otavio")
bd.inserir_clientes(2,"Rose")
#bd.__dados = "Outra coisa"
#print(bd.d__dados)
print(bd._BaseDeDados__dados)
bd.lista_clientes()