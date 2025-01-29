class Livro:
    def __init__(self, titulo, autor, ano, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel

    def emprestar(self):
        self.disponivel = False
        print(f"{self.titulo} foi emprestado!")

    def devolver(self):
        if self.disponivel:
            self.disponivel = True
            print(f"{self.titulo} foi devolvido.")
        else:
            print(f"{self.titulo} não está disponivel para empréstismo.")

    def informacoes(self):
        print(f"\nTítulo: {self.titulo}")
        print(f"Autor = {self.autor}")
        print(f"Ano: {self.ano}")
        print(f"Disponibilidade: {self.disponivel}\n")

livro1 = Livro(titulo="O Senhor dos Aneis", autor="J.R.R. Tolkien", ano=1954, disponivel=True)
livro2 = Livro(titulo="Harry Potter e a Pedra Filosofal", autor="J.K. Rowling", ano=1997, disponivel=True)

livro1.emprestar()
livro1.informacoes()

livro2.informacoes()
livro2.emprestar()
livro2.devolver()
livro2.informacoes()