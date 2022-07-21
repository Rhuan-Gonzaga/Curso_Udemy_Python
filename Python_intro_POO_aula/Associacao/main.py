from classes import Escritor,Caneta,MaquinaEscrever

escritor = Escritor("Rhuan")
caneta = Caneta("BIC")
maquina = MaquinaEscrever()

#Associalçao
escritor.ferramenta = caneta
escritor.ferramenta.escrever()