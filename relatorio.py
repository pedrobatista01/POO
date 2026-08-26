class Relatorio:

    @staticmethod
    def gerar_projeto(projeto):
        total = projeto.total_tarefas()
        concluidas = projeto.tarefas_concluidas()
        pendentes = projeto.tarefas_pendentes()
        andamento = projeto.tarefas_em_andamento()

        print("\n")
        print("=" * 60)
        print("             RELATÓRIO DO PROJETO")
        print("=" * 60)

        print(f"Projeto: {projeto.nome}")
        print(f"Responsável: {projeto.usuario.nome}")
        print(f"Total de tarefas: {total}")
        print(f"Tarefas concluídas: {concluidas}")
        print(f"Tarefas em andamento: {andamento}")
        print(f"Tarefas pendentes: {pendentes}")
        print(f"Progresso: {projeto.calcular_progresso():.2f}%")

        print("=" * 60)

    @staticmethod
    def gerar_geral(gerenciador):
        total_projetos = 0
        total_tarefas = 0
        total_concluidas = 0
        total_andamento = 0
        total_pendentes = 0

        for usuario in gerenciador.usuarios:
            total_projetos += len(usuario.projetos)

            for projeto in usuario.projetos:
                total_tarefas += projeto.total_tarefas()
                total_concluidas += projeto.tarefas_concluidas()
                total_andamento += projeto.tarefas_em_andamento()
                total_pendentes += projeto.tarefas_pendentes()

        if total_tarefas > 0:
            produtividade = (total_concluidas / total_tarefas) * 100
        else:
            produtividade = 0

        print("\n")
        print("=" * 60)
        print("             RELATÓRIO GERAL")
        print("=" * 60)

        print(f"Total de usuários: {len(gerenciador.usuarios)}")
        print(f"Total de projetos: {total_projetos}")
        print(f"Total de tarefas: {total_tarefas}")
        print(f"Tarefas concluídas: {total_concluidas}")
        print(f"Tarefas em andamento: {total_andamento}")
        print(f"Tarefas pendentes: {total_pendentes}")
        print(f"Produtividade geral: {produtividade:.2f}%")

        print("=" * 60)
