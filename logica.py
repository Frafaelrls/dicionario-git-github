from dicionario import dic


def devolve_significado(entrada):
    banco_dados = dic()
    if entrada in banco_dados:
        print(banco_dados[entrada])
    else:
        print("Palavra não encontrada")
