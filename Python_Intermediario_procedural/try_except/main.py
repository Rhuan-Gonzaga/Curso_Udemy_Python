#try e except

try:
    a ={}
    try:
        a = 1/0
    except:
        print("Erro")
except NameError as erro:
    print("Erro do desenvolvedor")
except (IndexError, KeyError) as erro:
    print("Erro de indice ou chave")
except Exception as erro:
    print("Ocorreu um erro indesperado")
finally:
    print("Sempre executada")
