class Loja:    
    #Variavel da classe
    valor = 150
    def __init__(self,marca_carro,cor):
        #Atributos/variaveis da instancia
        self.marca_carro = marca_carro
        self.cor = cor
    
    @classmethod
    def tipo_carro(cls, marca_carro,cor):
        preco =   cls.valor
        return cls(preco, marca_carro,cor)
        
#p1 = Pessoa_dados("Luiz", 32)
p1 = Loja.tipo_carro("Ferrari", "Vermelha")
print(p1.preco)