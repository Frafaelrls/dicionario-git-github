from dicionario import dic


def devolve_significado(entrada):
    banco_dados = dic()
    if entrada in banco_dados:
        print(banco_dados[entrada])

    if entrada == "?":
        lista = banco_dados.keys()
        for nomes in lista:
            print(nomes)
    else:
        print("Palavra não encontrada")
