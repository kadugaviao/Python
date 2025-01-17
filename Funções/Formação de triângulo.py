"""
Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas 
e diga ao usuário se elas podem ou não formar um triângulo.
"""

def retas():
    while True:
        try:
            r1 = float(input("Comprimento reta 1: "))
            r2 = float(input("Comprimento reta 2: "))
            r3 = float(input("Comprimento reta 3: "))
            if r1 > 0 and r2 > 0 and r3 > 0:
                return r1, r2, r3
            else:
                print("Erro. Os valores devem ser positivos. Tente novamente.")
        except ValueError:
            print("Erro. Apenas valores númericos são aceitos. Tente novamente.")

def formacao(r1, r2, r3):
    if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
        return "Os segmentos podem formar um triângulo."
    else:
        return "Os segmentos não podem formar um triângulo."

def main():
    r1, r2, r3 = retas()
    print(formacao(r1, r2, r3))

main()