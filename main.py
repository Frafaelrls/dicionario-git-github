from logica import devolve_significado


def user():
    entrada = ""
    while entrada != "Sair":
        entrada = input(f"Olá,\nInsira a palavra desejada ou digite 'Sair'\n")
        devolve_significado(entrada)


user()
