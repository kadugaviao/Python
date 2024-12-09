"""
Escreva um programa que leia o ano de nascimento de uma pessoa e
informe se ela pode votar, considerando que a pessoa deve ter 16 anos
ou mais para votar.

Exercício 7
"""
from datetime import datetime

anoDeNascimento = int(input('Digite o seu ano de nascimento: '))
anoAtual = datetime.now().year
idade = anoAtual - anoDeNascimento

if 18 <= idade <= 122:
    print(f'Você tem {idade} anos, pode votar!')
elif (idade < 18) and (idade >= 0):
    print(f'Você tem {idade} anos, não pode votar!')
else:
    print(f'Erro no Sistema!')
