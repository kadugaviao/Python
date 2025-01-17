"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""

from datetime import date

def data():
    while True:
        try:
            ano = int(input("Qual ano quer analisar? Coloque 0 para analisar o ano atual: "))
            if ano == 0: 
                return date.today().year
            elif ano > 0:
                return ano
            else: 
                print("Ano inválido. Coloque um ano depois de cristo.")
        except ValueError:
            print("Insira um um ano válido")

def bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano de {ano} é bissexto.")
    else:
        print(f"O ano de {ano} não é bissexto.")

def main():
    ano = data()
    bissexto(ano)

main()
