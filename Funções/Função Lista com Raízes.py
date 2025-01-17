from math import sqrt, floor, ceil

def num_raiz():
    listaRaizes = []
    while len(listaRaizes) < 10:
        try:
            num = int(input("Digite um número positivo: "))
            if num < 0:
                print("Por favor, insira um número positivo. ")
                continue
            raiz = sqrt(num)
            listaRaizes.append(raiz)
            print(f"Raiz quadrada de {num} = {raiz}")
            print(f"Raiz arredondada para cima: {floor(raiz)}")
            print(f"Raiz arredondada para baixo: {ceil(raiz)}")
        except ValueError:
            print("Por favor, insira um número válido.")

    print(f"\nLista de raízes calculadas: \n{listaRaizes}")

num_raiz()
