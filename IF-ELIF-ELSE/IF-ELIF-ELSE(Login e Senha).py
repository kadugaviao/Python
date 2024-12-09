"""
Escreva um programa que solicite o login e a senha do usuário. Se o
login for "admin" e a senha for "password", exiba "Acesso liberado",
caso contrário, exiba "Acesso negado".

Exercício 10
"""

login = input('Login: ')
senha = input('Senha: ')

if (login == 'admin') and (senha == 'password'):
    print('Acesso liberado!')
else:
    print('Acesso Negado!')
