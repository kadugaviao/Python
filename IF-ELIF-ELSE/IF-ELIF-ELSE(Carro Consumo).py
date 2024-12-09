"""
Desenvolva um programa que leia o custo de fábrica de um carro e
calcule o custo ao consumidor, somando o percentual do distribuidor
(28%) e impostos (45%).
O custo ao consumidor de um carro novo é a soma do custo de fábrica
com a percentagem do distribuidor e dos impostos (aplicados ao custo
de fábrica).
Supondo que a percentagem do distribuidor seja de 28% e os impostos
de 45%, escrever um algoritmo que leia o custo de fábrica de um carro
e escreva o custo ao consumidor.
Leia o custo de fábrica > Pegue o custo de fábrica e faça vezes 1,73
Apresente o custo ao consumidor.
"""

custoFabrica = float(input('Digite o custo de fabricação: '))
porcentagemDistribuidor = 0.28
impostos = 0.45

custoConsumidor = custoFabrica * (1 + porcentagemDistribuidor + impostos)

print(f'O custo do consumidor é: R${custoConsumidor:.2f}')
print(f'O valor do distribuidor é: {porcentagemDistribuidor}, imposto é {impostos}, valor de fábrica é {custoFabrica}.')
