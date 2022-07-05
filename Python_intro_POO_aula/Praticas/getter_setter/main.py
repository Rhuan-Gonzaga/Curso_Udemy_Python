 
class Nota_aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        
    
    def mostrar_media(self):
        media = (self.nota1 + self.nota2) / 2
        
        if media >= 7:
            print(f"Aluno {self.nome} APROVADO com media {media}")
        else:
            print(f"Aluno {self.nome} REPROVADO com media {media}")
            
    #Getter 1 
    @property
    def nota1(self):
        return self._nota1
    
    #Setter
    @nota1.setter
    def nota1(self, n1):
        #Verificando se o meu atributo nota1 é do tipo str e transformando em float
        if isinstance(n1, str):
            n1  = float(n1)
        self._nota1 = n1
    
    #Getter 2
    @property
    def nota2(self):
        return self._nota2
    
    #Setter
    @nota2.setter
    def nota2(self, n2):
        #Verificando se o meu atributo nota2 é do tipo str e transformando em float
        if isinstance(n2, str):
            n2  = float(n2)
        self._nota2 = n2
            
    
p1 = Nota_aluno("Rhuan", 7.0, "7.0")
p1.mostrar_media()