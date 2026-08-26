class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.projetos = []

    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)

    def remover_projeto(self, indice):
        if 0 <= indice < len(self.projetos):
            return self.projetos.pop(indice)

        return None

    def listar_projetos(self):
        if not self.projetos:
            print("Este usuário não possui projetos.")
            return

        print(f"\nPROJETOS DE {self.nome.upper()}")

        for i, projeto in enumerate(self.projetos, start=1):
            print(f"\nProjeto {i}")
            projeto.exibir()

    def exibir(self):
        print("-" * 50)
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Projetos: {len(self.projetos)}")
        print("-" * 50)
