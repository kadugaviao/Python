# Definindo a classe cachorro
class Cachorro:
    def __init__(self, nome, comida, sono):
        # construtor da classe para iniciar os atributos
        self.nome = nome
        self.comida = comida
        self.sono = sono

    # metodo para simular cachorro comendo.
    def comer(self):
        if self.comida > 0:
            self.comida -= 1
            print(f"{self.nome} comeu! Quantidade de comida restante: {self.comida}")
        else:
            print(f"{self.nome} não tem mais comida")
    
    # metodo para simular cachorro dormindo.
    def dormir(self):
        self.sono = False
        print(f"{self.nome} agora está dormindo.")
    
    # metodo para mostrar estado atual do cachorro.
    def status(self):
        print(f"{self.nome} - Comida: {self.comida}, Sono: {self.sono}")

cachorro1 = Cachorro(nome="Bolt", comida=5, sono=True)
cachorro2 = Cachorro(nome="Klaus", comida=3, sono=False)

cachorro1.comer()
cachorro1.comer()
cachorro1.dormir()

cachorro2.comer()

print(f"\nCachorro Nº1: {cachorro1.nome}")
print(f"Comida: {cachorro1.comida}")
print(f"Sono: {cachorro1.sono}")

print(f"\nCachorro Nº2: {cachorro2.nome}")
print(f"Comida: {cachorro2.comida}")
print(f"Sono: {cachorro2.sono}")

cachorro1.status()
cachorro2.status()