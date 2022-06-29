

class Caneta:
    def __init__(self,marca,cor,tampada=True,escrevendo=False):
        self.marca = marca
        self.cor = cor
        self.tampada = tampada
        self.escrevendo = escrevendo
    
    
    def destampar(self):
        if self.tampada:
            print(f"A caneta {self.marca} foi destampada")
            self.tampada = False
        else:
            print("A caneta já está destampada")
    
    def tampar(self):
        if not self.tampada:
            print(f"A caneta {self.marca} foi tampada")
            self.tampada = True
        else:
            print("A caneta já está tampada")
    
    def escrever(self):
        if not self.tampada:
            print("Vc está escrevendo ...")
            self.escrevendo = True
        if self.tampada:
            print("Vc precisa destampar a caneta")
            