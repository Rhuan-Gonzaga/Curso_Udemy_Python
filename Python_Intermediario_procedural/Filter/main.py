lista = [1,2,3,4,5,6,7,8,9,10]

produtos = [

    {"nome": "p1", "preco": 13},
    {"nome": "p2", "preco": 55.55},
    {"nome": "p3", "preco": 5.59},
    {"nome": "p4", "preco": 22},
    {"nome": "p5", "preco": 81.23},
    {"nome": "p6", "preco": 5.7},
    {"nome": "p7", "preco": 10.90},
    {"nome": "p8", "preco": 89.82},
    {"nome": "p9", "preco": 12},
    {"nome": "p10", "preco": 2.90},

]

#Filtra a minha lista, me retornando valores maiores q 5
nova_lista = filter(lambda x: x > 5, lista)



#Filtra os preços < 10
novos_preco = filter(lambda p: p["preco"] < 10, produtos)
print(list(novos_preco))

