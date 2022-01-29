from logica import devolve_significado, sair, apagar


def user():
    apagar()
    while True:
        entrada = input(f"\nOlá,\nInsira a palavra desejada."
                        f"\nDigite 'Sair' para encerrar o programa."
                        f"\nDigite '?' para acessar a lista de palavras"
                        f" salvas.\n")
        entrada = entrada.lower()
        if entrada == "sair":
            sair()
            break
        devolve_significado(entrada)


user()
