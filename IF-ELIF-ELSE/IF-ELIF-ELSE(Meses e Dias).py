"""
Faça um programa que leia a idade de uma pessoa e apresente o total
de meses e dias que ela já viveu. Considere que um ano tem 12 meses
e 365 dias.
Leia a idade da pessoa > Pege a idade e faça vezes 12.
Apresente o total de meses que a pessoa viveu.
Pegue a idade da pessoa > faça vezes 365.

Exercício 2

Apresente o total de dias que a pessoa viveu.
"""
idade = int(input('Digite sua idade: '))

vidaDias = idade * 365
vidaMeses = idade * 12

print(f'Você tem {idade} de idade!')
print(f'Você viveu {vidaDias} dias!')
print(f'Você viveu {vidaMeses} meses!')
