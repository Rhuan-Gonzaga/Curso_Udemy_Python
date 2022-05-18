"""
Pegando só os valores dos produtos do meu carrinho e somando
utilizando apenas List comprehension

"""
carrinho = []

carrinho.append(("Produto 1",30))
carrinho.append(("Produto 2",20))
carrinho.append(("Produto 3",50))
carrinho.append(("Produto 4",50))


preco = sum([float(y) for  x,y in carrinho])
print(preco)
 
