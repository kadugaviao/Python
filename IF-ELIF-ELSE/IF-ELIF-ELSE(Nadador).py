"""
Escreva um programa que leia a idade de um nadador e classifique-o
em uma das categorias: Infantil A (5-7 anos), Infantil B (8-10 anos),
Juvenil A (11-13 anos), Juvenil B (14-17 anos), ou Adulto (maiores de 18
anos).

Exercício 4
"""

idadeNadador = int(input(f'Digite a idade do nadador: '))

if idadeNadador < 5:
    print("Nadador é jovem demais para competir!")
elif 5 <= idadeNadador <= 7:
    print("Nadador é da categoria Infantil A!")
elif 8 <= idadeNadador <= 10:
    print("Nadador é da categoria Infantil B!")
elif 11 <= idadeNadador <= 13:
    print("Nadador é da categoria Juvenil A!")
elif 14 <= idadeNadador <= 17:
    print("Nadador é da categoria Juvenil B!")
else:
    print("Nadador é da categoria Adulto!")
