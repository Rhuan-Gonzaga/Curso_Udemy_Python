""""
1 -  Crie uma função1 que recebe uma função2 como parametro e retorne o valor da função2 executada
"""

##def ola_mundo():  #Função2
#    return "Olá mundão!"
#
#def mestre(funcao2): #Função1
#    return funcao2()
#
#executando = mestre(ola_mundo)
#print(executando)

"""
2 - Crie uma função1 que recebe uma função2 como parametro e retorne o valor da função executada. Faça a função1 executar duas funções que recebam um numero diferente de argumentos
"""

def mestre(funcao, *args,**kwargs):  #Função 1
    return funcao(*args, **kwargs)

def fala_oi(nome):  #Função 2
    return f"oi {nome}"

def saudacao(nome, saudacao): #Função 3
    return f"{saudacao} {nome}"

executando = mestre(fala_oi, "Luiz")
executando2 = mestre(saudacao, "Luiz",saudacao="Bom dia")
print(executando)
print(executando2)










