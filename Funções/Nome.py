def pessoa():
    while True:
        nome = input("Digite seu nome: ").strip().title()
        if nome.replace(" ", "").isalpha():
            return nome
        else:
            print("Erro. Os únicos caracteres validos são letras.")

def acharNome(nome):
    procura = input("Qual sobrenome deseja verificar? ").strip().title()
    if procura.replace(" ", "").isalpha():
        if procura in nome:
            print(f"O nome {nome} contem o sobrenome {procura}.")
    else:
        print(f"{nome} não tem o sobrenome {procura}.")

def main():
    nome = pessoa()
    acharNome(nome)

main()