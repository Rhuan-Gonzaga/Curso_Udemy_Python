class Pessoa_dados:    
    #Variavel da classe
    ano_atual = 2022
    def __init__(self,nome,idade):
        #Atributos/variaveis da instancia
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        #Metodo de instancia(depende da minha instancia/OBJ)
        print(self.ano_atual - self.idade)
    
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade =  cls.ano_atual - ano_nascimento
        return cls(nome, idade)
        
#p1 = Pessoa_dados("Luiz", 32)
p1 = Pessoa_dados.por_ano_nascimento("Luiz", 1987)
print(p1.idade)
p1.get_ano_nascimento()