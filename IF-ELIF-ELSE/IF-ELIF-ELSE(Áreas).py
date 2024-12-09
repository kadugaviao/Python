"""
Crie um programa que calcule a área de uma sala, quarto e banheiro,
somando as áreas para apresentar o total. Para cada ambiente, leia a
largura e o comprimento.

Exercício 5

"""

larguraSala = float(input('Digite a largura da sala: '))
comprimentoSala = float(input('Digite o comprimento da sala: '))
areaSala = larguraSala * comprimentoSala

larguraQuarto = float(input('Digite a largura do quarto: '))
comprimentoQuarto = float(input('Digite o comprimento do quarto: '))
areaQuarto = larguraQuarto * comprimentoQuarto

larguraBanheiro = float(input('Digite a largura do banheiro: '))
comprimentoBanheiro = float(input('Digite o comprimento do banheiro: '))
areaBanheiro = larguraBanheiro * comprimentoBanheiro

areaTotal = areaSala + areaQuarto + areaBanheiro
print(f'A área total é {areaTotal:.2f}')
