from random import choice

def listaAlunos():
    lista = []
    while len(lista) < 4: 
            nomes = input(f"{len(lista) + 1}º Aluno(a): ").strip()
            if nomes: 
                lista.append(nomes)
            else: 
                print("Digite um nome válido, não podem estar vazio ou conter apenas espaços.")
    return lista

def aleatorio(lista):
    escolhido = choice(lista)
    print(f"{escolhido} foi o aluno(a) escolhido(a)!")

def main():
    lista = listaAlunos()
    aleatorio(lista)

main()