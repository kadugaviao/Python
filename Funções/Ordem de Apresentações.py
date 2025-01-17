from random import shuffle

def listaOrdem():
    lista = []
    while len(lista) < 4:
        nomes = input(f"{len(lista) + 1}º Aluno(a): ").strip()
        if nomes:
            lista.append(nomes)
        else:
            print("Digite um nome válido, estar vazio ou conter somente espaços.")
    return lista

def embaralhar(lista):
    shuffle(lista)
    print(f"Ordem de Apresentações: {', '.join(lista)} ")

def main():
    lista = listaOrdem()
    embaralhar(lista)

main()



