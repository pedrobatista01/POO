from datetime import datetime
from enums import Prioridade, Status


class Tarefa:
    def __init__(self, titulo, descricao, prioridade=Prioridade.MEDIA):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = Status.PENDENTE
        self.data_criacao = datetime.now()

    def alterar_status(self, novo_status):
        self.status = novo_status

    def alterar_prioridade(self, nova_prioridade):
        self.prioridade = nova_prioridade

    def esta_concluida(self):
        return self.status == Status.CONCLUIDA

    def exibir(self):
        print("-" * 50)
        print(f"Título: {self.titulo}")
        print(f"Descrição: {self.descricao}")
        print(f"Prioridade: {self.prioridade.value}")
        print(f"Status: {self.status.value}")
        print(
            f"Data de criação: "
            f"{self.data_criacao.strftime('%d/%m/%Y %H:%M')}"
        )
        print("-" * 50)
