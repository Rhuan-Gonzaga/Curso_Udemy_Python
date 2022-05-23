from dados import produtos,pessoas,lista

#Função map com Lista
nova_lista = map(lambda x: x * 2, lista)
#print(list(nova_lista))

#Função map com dicionarios
novo_valor = map(lambda p: p["preco"] * 2, produtos)
#print(list(novo_valor))

#Passando a função map sem alterar a estrutura do dict, só o preco
def aumentar_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p

precos = map(aumentar_preco, produtos)

for produto in precos:
    #print(produto)
    pass

#Pegando só o nome de pessoas
pessoa = map(lambda nome: nome["nome"], pessoas)
print(list(pessoa))

