from math import radians, sin, cos, tan

def valor():
    angulo = float(input("Digite o ângulo que você deseja: "))
    seno = sin(radians(angulo))
    cosseno = cos(radians(angulo))

    print(f"\nO seno do ângulo de {angulo}º graus é: {seno:.2f}")
    print(f"\nO cosseno do ângulo de {angulo}º graus é: {cosseno:.2f}")

    if cosseno == 0:
        print("A tangente é indefinida para esse ângulo.")
    else:
        tangente = tan(radians(angulo))
        print(f"\nA tangente do ângulo de {angulo}º graus é: {tangente:.2f}")

valor()