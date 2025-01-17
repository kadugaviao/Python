"""
Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.
"""

def radar():
    while True: 
        try:
            velocidade = int(input("Velocidade do carro: "))
            if velocidade < 0:
                print("Erro no radar. Velocidade ínvalida.")
            else: 
                return velocidade
        except ValueError:
            print("Por favor, insira um número válido.")

def multado(velocidade):
    if velocidade > 80:
        diferenca = velocidade - 80
        multa = diferenca * 7
        print(f"Limite ultrapassado: {velocidade}Km/h. Multa: R${multa:.2f}")
    else: 
        print(f"Velocidade registrada: {velocidade} Km/h. Nenhuma multa registrada.")

def main():
    velocidade = radar()
    multado(velocidade)
        
main()

