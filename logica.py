from dicionario import dic
import os


def apagar():
    limpar = "clear"  # Se for mac ou linux
    if os.name in ("nt", "dos"):  # Se for windows
        os.system('cls')
    else:
        os.system(limpar)


def devolve_significado(entrada):
    banco_dados = dic()
    if entrada in banco_dados:
        apagar()
        print(f"{entrada}:")
        print(banco_dados[entrada])

    elif entrada == "?":
        apagar()
        lista = banco_dados.keys()
        for nomes in lista:
            print(nomes)
    else:
        apagar()
        print("Palavra não encontrada")
