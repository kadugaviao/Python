"""
Faça um programa que leia a quantidade de um produto adquirida e o
preço unitário. Calcule o valor total e o desconto aplicável:
2% se a quantidade for até 5.
3% se a quantidade estiver entre 6 e 10.
5% se a quantidade for maior que 10.

Exercício 11
"""

quantidadeProduto = int(input(f'Quantas unidades foram compradas: '))
precoUnitario = float(input(f'Preço por unidade: '))
precoFinal = precoUnitario * quantidadeProduto

if (quantidadeProduto > 0) and (quantidadeProduto <= 5):
    desconto = precoFinal * 0.02
elif 5 < quantidadeProduto <= 10:
    desconto = precoFinal * 0.03
else:
    desconto = precoFinal * 0.05

totalPagar = precoFinal - desconto
print(f'Preço final do produto é R${totalPagar}!')
