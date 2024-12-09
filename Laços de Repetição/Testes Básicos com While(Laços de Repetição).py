"""
valor = 0

while (valor < 5):
    print(f'Valor: {valor}')
    valor += 1
print(f'Valor fora do WHILE: {valor}')
"""

"""
valor = 0 

while valor < 100:
    if valor % 2 == 0 
        print('Valor: {valor}')
    valor = valor + 1
"""

"""
num = int(input('Digite um número: '))
i = 0

while (i <= 10):
    tabuada = num * i
    print(f'1 . {i} = {tabuada}')
    i += 1
"""

"""
valor = 0

while valor < 5000:
    if valor % 742 == 0:
        print(f'Valor: {valor}')
    valor += 1
"""

"""
somaNotas = 0
i = 0

while i < 3:
    nota = float(input('Digite uma nota: '))
    somaNotas = somaNotas + nota
    i += 1
print(f'A soma das notas é: {somaNotas}')

media = somaNotas / 3
print(f'A média do aluno é: {media}')
"""

opcao = 0

while opcao != 3:
    print('1 - Soma de valores')
    print('2 - Subtração de valores')
    print('3 - Sair')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        soma = n1 + n2
        print(f'Soma dos valores: {soma}')
    elif opcao == 2:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        subtracao = n1 - n2
        print(f'Subtração dos valores: {subtracao}')
    elif opcao == 3:
        print('Saindo do programa...')
    else:
        print('Opção Invalida')
