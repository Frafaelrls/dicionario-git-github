# criar um arquivo para lógica.py
def dic(palavra):
    if user_input in dicionario:
        print(dicionario[user_input])
    else:
        print(f"Palavra não encontrada!")

# Manter no arquivo dicionario.py
dicionario = {'git push': 'Envia as alterações locais para do repositório local para o remoto', 'teste 2': 'Significado dois'}
# Enviar para arquivo main.py
user_input = input(f"Olá,\nInsira a palavra desejada\n")
dic(user_input)
