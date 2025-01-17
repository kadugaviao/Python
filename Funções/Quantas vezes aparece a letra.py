"""
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""

def frase():
    while True:
        f = input("Digite uma frase: ").strip().lower()
        if f.replace(" ", "").isalpha():
            return f
        else:
            print("Erro. Digite uma frase válida.")

def acharLetra(f):
    while True:
        letra = input("Digite a letra que será encontrada: ").strip().lower()
        if len(letra) == 1 and letra.isalpha():
            quant = f.count(letra)
            print(f"A letra 'a' aparece {quant} vezes na frase!")
            if quant > 0:
                print(f"A primeira posição é {f.find(letra)}.")
                print(f"A ultima posição é {f.rfind(letra)}.")
            else:
                print(f"A letra {letra} não foi encontrada na frase")
            break

def main():
    f = frase()
    acharLetra(f)

main()