from enums import Status


class Projeto:
    def __init__(self, nome, descricao, usuario):
        self.nome = nome
        self.descricao = descricao
        self.usuario = usuario
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            return self.tarefas.pop(indice)

        return None

    def listar_tarefas(self):
        if not self.tarefas:
            print("Este projeto não possui tarefas.")
            return

        print(f"\nTAREFAS DO PROJETO: {self.nome}")

        for i, tarefa in enumerate(self.tarefas, start=1):
            print(f"\nTarefa {i}")
            tarefa.exibir()

    def calcular_progresso(self):
        if len(self.tarefas) == 0:
            return 0

        concluidas = sum(
            1
            for tarefa in self.tarefas
            if tarefa.status == Status.CONCLUIDA
        )

        return (concluidas / len(self.tarefas)) * 100

    def total_tarefas(self):
        return len(self.tarefas)

    def tarefas_concluidas(self):
        return sum(
            1
            for tarefa in self.tarefas
            if tarefa.status == Status.CONCLUIDA
        )

    def tarefas_pendentes(self):
        return sum(
            1
            for tarefa in self.tarefas
            if tarefa.status == Status.PENDENTE
        )

    def tarefas_em_andamento(self):
        return sum(
            1
            for tarefa in self.tarefas
            if tarefa.status == Status.EM_ANDAMENTO
        )

    def exibir(self):
        print("-" * 60)
        print(f"Projeto: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Responsável: {self.usuario.nome}")
        print(f"Quantidade de tarefas: {self.total_tarefas()}")
        print(f"Progresso: {self.calcular_progresso():.2f}%")
        print("-" * 60)
