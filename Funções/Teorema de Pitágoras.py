from math import hypot

def trianguloRetangulo():
    co = float(input("\nDigite o comprimento do cateto oposto: "))
    ca = float(input("Digite o comprimento do cateto adjacente: "))
    hi = hypot(co, ca)
    print(f"\nO comprimento da hipotenusa é: {hi:.2f}")

trianguloRetangulo()

"""
def trianguloRetangulo():
    co = float(input("\nDigite o comprimento do cateto oposto: "))
    ca = float(input("Digite o comprimento do cateto adjacente: "))
    hi = (co ** 2 + ca ** 2) ** (1/2)
    print(f"\nO comprimento da hipotenusa é: {hi:.2f}")

trianguloRetangulo()
"""