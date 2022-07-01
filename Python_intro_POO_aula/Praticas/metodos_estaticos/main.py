
class Maior:
    def __init__(self,nome):
        self.nome = nome

    @staticmethod
    def verificar_idade(idade):
        if idade >= 18:
            print("Vc pode comprar bebida alcoolica")
        else:
            print("Vc n pode comprar bebida alcoolica")


#Maior.verificar_idade(22)
pessoa = Maior("Rhuan")
pessoa.verificar_idade(15)