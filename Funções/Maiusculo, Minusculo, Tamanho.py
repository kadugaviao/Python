"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.
"""

def pessoa():
    while True:
        nome = input("Digite um nome: ").strip()
        if nome.replace(" ", "").isalpha(): 
            print("Analisando nome...")
            return nome
        else: 
            print("Erro. tente novamente!")

def maiusculoMinusulo(nome):
    print(f"\nNome maiúsculo: {nome.upper()}")
    print(f"Nome minúsculo: {nome.lower()}")

def semEspaços(nome):
    separado = nome.replace(" ", "")
    print(f"\nTamanho sem espaços: {len(separado)}")

def primeiroNome(nome):
    primeiro = nome.split()[0]
    print(f"\nSeu primeiro nome é {primeiro} e ele tem {len(primeiro)} letras.")

def main():
    nome = pessoa()
    maiusculoMinusulo(nome)
    semEspaços(nome)
    primeiroNome(nome)

main()



