from random import randint
class Pessoa_dados:    
    #Variavel da classe
    ano_atual = 2022
    
    #Metodo construtor
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    #Metodo de instancia(depende da minha instancia/OBJ)    
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
    
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade =  cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(50,100)
        return rand
    
p1 = Pessoa_dados.por_ano_nascimento("Luiz", 1987)
print(p1.idade)
p1.get_ano_nascimento()
print(p1.gera_id())
print(Pessoa_dados.gera_id())
