dicionario = {'git push': 'Envia as alterações locais para o repositório remoto', 'teste 2': 'Significado doi'}
print(dicionario['git push'])
print("Teste")
def dic(user_input):
    dicionario = {'teste': 'Significado um', 'teste 2': 'Significado dois'}
    print(dicionario[user_input])


user_input = input(f"Olá,\nInsira a palavra desejada\n")
dic(user_input)
