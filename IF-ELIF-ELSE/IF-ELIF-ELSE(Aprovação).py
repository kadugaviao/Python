"""
- Crie um programa que leia o nome de um aluno e três notas: a primeira
nota vale 5, a segunda nota vale 3, e a terceira vale 2. Calcule a média
ponderada e informe se o aluno está aprovado (média >= 7) ou
reprovado.
- Leia o nome do aluno > primeira nota do aluno > pegue a nota e faça
vezes 0,5 e armazene em uma variável.
- Leia a segunda nota do aluno > pegue a nota e faça vezes 0,3 e
armazene em uma variável.
- Leia a terceira nota do aluno > pegue a nota e faça vezes 0,2 e
armazene em uma variável.
- Some o obtenha o resultado das três notas.
Crie uma condição com if-elif-else:
- Se o aluno obter média maior ou igual a 7,0 > print("O aluno está
aprovado")
- Se o aluno obter menor que a 7,0 > print("O aluno está reprovado")

Exercício 1
"""

nomeDoAluno = input(f'Digite o nome do aluno: ')

nota1 = float(input(f'Digite a primeira nota(peso 0.5): '))
nota2 = float(input(f'Digite a segunda nota(peso 0.3): '))
nota3 = float(input(f'Digite a terceira nota(peso 0.2): '))

mediaPonderada = (nota1 * 0.5 + nota2 * 0.3 + nota3 * 0.2)

if 0 <= mediaPonderada < 7:
    print(f'A média é {mediaPonderada:.2f}, Aluno {nomeDoAluno} esta reprovado!')
elif (mediaPonderada >= 7.0) and (mediaPonderada <= 10):
    print(f'A média é {mediaPonderada:.2f}, Aluno 7{nomeDoAluno} aprovado!')
else:
    print(f'Houve um erro no sistema!')
