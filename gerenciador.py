from usuario import Usuario
from projeto import Projeto
from tarefa import Tarefa


class Gerenciador:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self, nome, email):
        usuario = Usuario(nome, email)
        self.usuarios.append(usuario)
        return usuario

    def listar_usuarios(self):
        if not self.usuarios:
            print("\nNenhum usuário cadastrado.")
            return

        print("\n========== USUÁRIOS ==========")

        for i, usuario in enumerate(self.usuarios, start=1):
            print(f"\nUsuário {i}")
            usuario.exibir()

    def remover_usuario(self, indice):
        if 0 <= indice < len(self.usuarios):
            return self.usuarios.pop(indice)

        return None

    def criar_projeto(self, nome, descricao, usuario):
        projeto = Projeto(nome, descricao, usuario)
        usuario.adicionar_projeto(projeto)
        return projeto

    def listar_projetos(self):
        encontrou = False

        for usuario in self.usuarios:
            for projeto in usuario.projetos:
                encontrou = True
                projeto.exibir()

        if not encontrou:
            print("\nNenhum projeto cadastrado.")

    def remover_projeto(self, usuario, indice):
        return usuario.remover_projeto(indice)

    def criar_tarefa(self, projeto, titulo, descricao, prioridade):
        tarefa = Tarefa(titulo, descricao, prioridade)
        projeto.adicionar_tarefa(tarefa)
        return tarefa

    def listar_todas_tarefas(self):
        encontrou = False

        for usuario in self.usuarios:
            for projeto in usuario.projetos:
                if projeto.tarefas:
                    encontrou = True
                    print("\n" + "=" * 60)
                    print(f"PROJETO: {projeto.nome}")
                    print("=" * 60)
                    projeto.listar_tarefas()

        if not encontrou:
            print("\nNenhuma tarefa cadastrada.")

    def buscar_usuario(self, indice):
        if 0 <= indice < len(self.usuarios):
            return self.usuarios[indice]

        return None

    def buscar_projeto(self, usuario, indice):
        if 0 <= indice < len(usuario.projetos):
            return usuario.projetos[indice]

        return None

    def buscar_tarefa(self, projeto, indice):
        if 0 <= indice < len(projeto.tarefas):
            return projeto.tarefas[indice]

        return None

    def alterar_status_tarefa(self, tarefa, status):
        tarefa.alterar_status(status)

    def alterar_prioridade_tarefa(self, tarefa, prioridade):
        tarefa.alterar_prioridade(prioridade)
