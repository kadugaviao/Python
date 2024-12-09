import random

numeroSorteio = random.randint(0, 50)

"""
numeroEscolhido = int(input('Digite seu número: ')

if (numeroEscolhido >= 0) and (numeroEscolhido <= 50):
    print(f"Seu número é {numeroEscolhido}!")
    margem = 5
    if numeroEscolhido == numeroSorteio:
        print(f'Você ganhou o sorteio!')
    elif abs(numeroEscolhido - numeroSorteio) <= margem:
        print(f'Esta perto, o número foi próximo.')
    else:
        print(f'Você perdeu o sorteio...')
else:
    print(f'Número {numeroEscolhido} não esta pode ser escolhido!')
"""

numeroSecreto = random. randint(0, 50)
palpite = -1
tentativa = 0

while palpite != numeroSecreto:
    palpite = int(input('Digite seu palpite, entre 0 a 50: '))
    tentativa += 1
    
    if palpite > numeroSecreto:
        print('Seu palpite é maior')
    elif palpite < numeroSecreto:
        print('Seu palpite é menor')
    else:
        print('Parabens! Seu número foi escolhido!')
print(f'Você acertou o número aleatório {numeroSecreto} em {tentativa} tentativas!')
