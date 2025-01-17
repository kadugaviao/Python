"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

def pagamento():
    while True:
        try:
            salario = float(input("Salário do funcionário: "))
            if salario >= 0:
                return salario
            else:
                print("Erro. O salário não pode ser negativo. Tente novamente.")
        except ValueError:
            print("Erro. Digite um valor numérico válido. Tente novamente.")

def acrescimo(salario):
    if salario > 1250:
        return salario * 1.10
    else:
        return salario * 1.15

def main():
    salario = pagamento()
    salarioAcrescimo = acrescimo(salario)

    print(f"Salário com acréscimo: R${salarioAcrescimo:.2f}")

main()