"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""

def viagem():
    while True: 
        try:
            distancia = float(input(f"Qual a distância da sua viagem(em Km): "))
            if distancia <= 0:
                print("A distância deve ser maior que 0. Tente novamente.")
            else:
                print(f"Você está prestes a iniciar uma viagem de {distancia}Km.")
                return distancia
        except ValueError:
            print("Erro. Digite um valor numérico válido.")

def preco(distancia):
    if distancia <= 200:
        precoTotal = distancia * 0.50
        print(f"Distância = {distancia} \nValor por Km = 0.50")
    elif distancia > 200:
        precoTotal = distancia * 0.45
        print(f"Distância = {distancia} \nValor por Km = 0.45")
    print(f"Total a pagar: R${precoTotal:.2f}")


def main():
    distancia = viagem()
    preco(distancia)

main()
