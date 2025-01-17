""" 
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

def lista():
    listaN = []
    return listaN 

def ler(listaN):
    while len(listaN) < 3:
        try:
            n = int(input("\nDigite um número: "))    
            listaN.append(n)
        except ValueError:
            print("Erro. Por favor, digite um valor númerico inteiro.")
    return listaN

def maiorMenor(listaN):
    print(f"\nO maior dos 3 valores é: {max(listaN)}")
    print(f"\nO menor dos 3 valores é: {min(listaN)}")

def main():
    listaN = lista()
    ler(listaN)
    maiorMenor(listaN)

main()

        
