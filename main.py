from logica import devolve_significado


def user():
    entrada = ""
    while entrada != "sair":
        entrada = input(f"\nOlá,\nInsira a palavra desejada."
                        f"\nDigite 'Sair' para encerrar o programa."
                        f"\nDigite '?' para acessar a lista de palavras"
                        f" salvas.\n")
        entrada = entrada.lower()
        if entrada != "sair":
            devolve_significado(entrada)


user()
