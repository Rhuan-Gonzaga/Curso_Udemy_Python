
perguntas = {

    "Pergunta 1": {
        #pv
        "pergunta": "Quanto é 2+2?",
        "respostas": {"a": "1", "b": "4" ,"c": "5"},
        "resposta_certa": "b",
    },

    
    "Pergunta 2": {
        #pv
        "pergunta": "Quanto é 3-2?",
        "respostas": {"a": "1", "b": "4" ,"c": "5"},
        "resposta_certa": "a",
    },

    "Pergunta 3": {
        #pv
        "pergunta": "Quanto é 3*2?",
        "respostas": {"a": "1", "b": "4" ,"c": "6"},
        "resposta_certa": "c",
    },
}

print()
respostas_certas = 0
#chave e valor 
for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")

    print("Respostas: ")
    for rk, rv in pv['respostas'].items():
        print(f"[{rk}]: {rv}")
   
    resposta_usuario = input("Sua resposta: ")

    if resposta_usuario == pv['resposta_certa']:
        print("Você ACERTOU!")
        respostas_certas +=1 
    else:
        print("Você ERROU!")

    print()

print(f"Você acertou {respostas_certas} de {len(perguntas)} perguntas")