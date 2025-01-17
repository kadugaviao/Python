"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint 
from time import sleep

def sorteio():
    computador = randint(0, 5)
    print("-=-" * 20)
    while True:
        try:    
            print("Vou pensar em número entre 0 e 5, tente advinhar...")
            print("-=-" * 20)
            palpite = int(input("Digite um número(entre 0 e 5): "))
            print("PROCESSANDO...")
            sleep(2)
            if palpite < 0 or palpite > 5:
                print("Número ínvalido. Tente novamente.")
            elif palpite == computador:
                print(f"Você ganhou! O número correto é {computador}")
                break
            else:
                print(f"Você perdeu! O número correto era {computador}")
                
                opc = input("Deseja jogar novamente(S/N)? ").strip().upper()
                if opc == 'S':
                    print("Reiniciando o jogo...\n")
                    sorteio = randint(0, 5)
                elif opc == 'N':
                    print("Obrigado por jogar. Saindo...")
                    break
                else:
                    print("Opção ínvalida. Responda apenas S/N!")
        except ValueError:
            print("Por favor, digite apenas números inteiros entre 0 e 5.")

sorteio()