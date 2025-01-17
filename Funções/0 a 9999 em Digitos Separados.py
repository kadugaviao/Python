"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

"""
# Matematicamente
def numero():
    while True:
        num = int(input("Digite um número: "))
        if 0 <= num <= 9999: # Verifica se um número é maior que 0 e menor que 9999
                return num
        else:
            print("Digite um número de 0 a 9999.")

def digitos(num):
    unidade = num % 10
    dezena = (num // 10) % 10
    centena = (num // 100) % 10
    milhar = (num // 1000) % 10

    print(f"Unidade: {unidade}")
    print(f"Dezena: {dezena}")
    print(f"Centena: {centena}")
    print(f"Milhar: {milhar}")

def main():
    num = numero()
    digitos(num)

main()
"""

# Como String
def numero():
    while True:
        num = int(input("Digite um número: "))
        if 0 <= num <= 9999: # Verifica se um número é maior que 0 e menor que 9999
                n = str(num)
                return n
        else:
            print("Digite um número de 0 a 9999.")

def digitos(n):
    print(f"Unidade: {n[3]}")
    print(f"Dezena: {n[2]}")
    print(f"Centena: {n[1]}")
    print(f"Milhar: {n[0]}")

def main():
    n = numero()
    digitos(n)

main()