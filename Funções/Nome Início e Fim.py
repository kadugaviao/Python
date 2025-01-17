"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida 
o primeiro e o último nome separadamente.
"""

def pessoa():
    while True:
        nome = input("Digite seu nome completo: ").strip().title()
        if nome.replace(" ", "").isalpha:
            return nome
        else:
            print("Erro, tente novamente. Digite um nome válido!")
    
def primeiroUltimo(nome):
    palavras = nome.split()
    primeiro = palavras[0]
    ultimo = palavras[-1]
    print(f"Seu primeiro nome é: {primeiro}")
    print(f"Seu último nome é: {ultimo}")

def main():
    nome = pessoa()
    primeiroUltimo(nome)

main()
