"""
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
"""

def nomeCidade():
    while True:
        cidade = input("Que cidade você nasceu? ").strip().title()
        if cidade.replace(" ", "").isalpha():
            return cidade
        else:
            print("Erro, tente novamente. O nome da cidade não pode conter caracteres inválidos.")

def primeiroNome(cidade):
    while True:
        palavra = input("Digite uma palavra: ").strip().title()
        if palavra.isalpha():
            if cidade.startswith(palavra):
                print(f"O nome da cidade começa com a palavra '{palavra}'")
            else:
                print(f"O nome da cidade não começa com a palavra '{palavra}'")
            break
        else:
            print("Erro, tente novamente. A palavra só pode conter letras.")

def main():
    cidade = nomeCidade()
    primeiroNome(cidade)

main()
