
#Passando o valor p var, com compressao
l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [var for var in l1]

#Dois for
ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

#Mudando os valor de A para @
l2 = ['Luiz','Mauro','Maria']
ex4 = [v.replace('a','@').upper() for v in l2]


#Invertando o lado dos valores
tupla = (

    ('Chave', 'valor'),
    ('Chave2', 'valor2')

)

ex5 = [(y, x) for x, y in tupla]

#Usando condição if na lista
l3 = list(range(100))
ex6 = [v for v in l3 if v % 2 == 0]

#Usando condição else na lista
ex7 = [v if v % 3 == 0 else "Não é" for v in l3]
print(ex7)