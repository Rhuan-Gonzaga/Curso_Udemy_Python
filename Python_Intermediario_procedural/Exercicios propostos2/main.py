"""
lista = ["0123456789", "0123456789","0123456789","0123456789","0123456789",]
retorno = "0123456789.0123456789.0123456789.0123456789.0123456789.0123456789."

"""

string = "01234567890123456789012345678901234567890123456789"

lista = [string[i:i + 10] for i in range(0, len(string), 10)]
retorno = ".".join(lista)

print(lista)
print(retorno)
