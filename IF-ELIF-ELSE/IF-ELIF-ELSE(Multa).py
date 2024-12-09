"""
Crie um programa que leia a velocidade de um carro e aplique as
seguintes penalidades:

Mais de 120 km/h: Multa de R$1000,00 e 7 pontos na carteira.
Mais de 100 km/h: Multa de R$750,00 e 5 pontos na carteira.
Mais de 80 km/h: Multa de R$500,00 e 4 pontos na carteira.

Exercício 8
"""

velocidadeCarro = float(input(f'A velocidade do carro foi: '))

if (velocidadeCarro < 80) and (velocidadeCarro > 0):
    print('Sem multa!')
elif 80 <= velocidadeCarro <= 99:
    print('Multa de 80km, R$500 e 4 pontos na carteira!')
elif 100 <= velocidadeCarro <= 119:
    print('Multa de 100km, R$750 e 5 pontos na carteira!')
elif 120 <= velocidadeCarro <= 200:
    print('Multa de 120km, R$1000 e 7 pontos na carteira!')
