"""
Desenvolva um programa que leia o total de horas trabalhadas no mês
e calcule o salário final de um funcionário que recebe R$35,00 por
hora. Caso o salário seja menor que R$1000,00, adicione um aumento
de R$300,00.3

Exercício 9
"""

totalHorasMes = float(input('Digite o total de horas mensais: '))

salarioFuncionario = 35.00 * totalHorasMes
aumento = 300

if (salarioFuncionario < 1000.00) and (salarioFuncionario >= 0):
    salarioFuncionario = salarioFuncionario + aumento
    print(f'Seu salário é R${salarioFuncionario:.2f}!')
elif salarioFuncionario >= 1000:
    print(f'Seu salário é R${salarioFuncionario:.2f}!')
else:
    print('Operação Invalida!')
