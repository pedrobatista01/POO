from gerenciador import Gerenciador
from relatorio import Relatorio
from enums import Prioridade, Status


gerenciador = Gerenciador()


def pausar():
    input("\nPressione ENTER para continuar...")


def escolher_prioridade():
    print("\nEscolha a prioridade:")
    print("1 - Baixa")
    print("2 - Média")
    print("3 - Alta")

    opcao = input("Opção: ")

    if opcao == "1":
        return Prioridade.BAIXA

    if opcao == "2":
        return Prioridade.MEDIA

    if opcao == "3":
        return Prioridade.ALTA

    print("Opção inválida. Prioridade Média selecionada.")
    return Prioridade.MEDIA


def escolher_status():
    print("\nEscolha o novo status:")
    print("1 - Pendente")
    print("2 - Em andamento")
    print("3 - Concluída")

    opcao = input("Opção: ")

    if opcao == "1":
        return Status.PENDENTE

    if opcao == "2":
        return Status.EM_ANDAMENTO

    if opcao == "3":
        return Status.CONCLUIDA

    return None


def selecionar_usuario():
    if not gerenciador.usuarios:
        print("\nNenhum usuário cadastrado.")
        return None

    gerenciador.listar_usuarios()

    try:
        indice = int(input("\nDigite o número do usuário: ")) - 1
    except ValueError:
        print("Digite um número válido.")
        return None

    usuario = gerenciador.buscar_usuario(indice)

    if usuario is None:
        print("Usuário não encontrado.")

    return usuario


def selecionar_projeto():
    usuario = selecionar_usuario()

    if usuario is None:
        return None

    if not usuario.projetos:
        print("\nEsse usuário não possui projetos.")
        return None

    usuario.listar_projetos()

    try:
        indice = int(input("\nDigite o número do projeto: ")) - 1
    except ValueError:
        print("Digite um número válido.")
        return None

    projeto = gerenciador.buscar_projeto(
        usuario,
        indice
    )

    if projeto is None:
        print("Projeto não encontrado.")

    return projeto


def selecionar_tarefa():
    projeto = selecionar_projeto()

    if projeto is None:
        return None

    if not projeto.tarefas:
        print("\nEsse projeto não possui tarefas.")
        return None

    projeto.listar_tarefas()

    try:
        indice = int(input("\nDigite o número da tarefa: ")) - 1
    except ValueError:
        print("Digite um número válido.")
        return None

    tarefa = gerenciador.buscar_tarefa(
        projeto,
        indice
    )

    if tarefa is None:
        print("Tarefa não encontrada.")

    return tarefa


# ==========================================
# MENU DE USUÁRIOS
# ==========================================

def cadastrar_usuario():
    print("\n========== CADASTRAR USUÁRIO ==========")

    nome = input("Nome: ")
    email = input("E-mail: ")

    if not nome or not email:
        print("Nome e e-mail são obrigatórios.")
        return

    gerenciador.cadastrar_usuario(nome, email)

    print("\nUsuário cadastrado com sucesso!")


def remover_usuario():
    print("\n========== REMOVER USUÁRIO ==========")

    usuario = selecionar_usuario()

    if usuario is None:
        return

    gerenciador.usuarios.remove(usuario)

    print("\nUsuário removido com sucesso!")


# ==========================================
# MENU DE PROJETOS
# ==========================================

def criar_projeto():
    print("\n========== CRIAR PROJETO ==========")

    usuario = selecionar_usuario()

    if usuario is None:
        return

    nome = input("Nome do projeto: ")
    descricao = input("Descrição do projeto: ")

    if not nome:
        print("O nome do projeto é obrigatório.")
        return

    gerenciador.criar_projeto(
        nome,
        descricao,
        usuario
    )

    print("\nProjeto criado com sucesso!")


def listar_projetos():
    print("\n========== PROJETOS ==========")

    gerenciador.listar_projetos()


def remover_projeto():
    print("\n========== REMOVER PROJETO ==========")

    usuario = selecionar_usuario()

    if usuario is None:
        return

    if not usuario.projetos:
        print("Esse usuário não possui projetos.")
        return

    usuario.listar_projetos()

    try:
        indice = int(
            input("\nDigite o número do projeto: ")
        ) - 1
    except ValueError:
        print("Digite um número válido.")
        return

    projeto = gerenciador.remover_projeto(
        usuario,
        indice
    )

    if projeto:
        print("\nProjeto removido com sucesso!")
    else:
        print("\nProjeto não encontrado.")


# ==========================================
# MENU DE TAREFAS
# ==========================================

def criar_tarefa():
    print("\n========== CRIAR TAREFA ==========")

    projeto = selecionar_projeto()

    if projeto is None:
        return

    titulo = input("Título da tarefa: ")
    descricao = input("Descrição: ")

    if not titulo:
        print("O título da tarefa é obrigatório.")
        return

    prioridade = escolher_prioridade()

    gerenciador.criar_tarefa(
        projeto,
        titulo,
        descricao,
        prioridade
    )

    print("\nTarefa criada com sucesso!")


def listar_tarefas():
    print("\n========== TODAS AS TAREFAS ==========")

    gerenciador.listar_todas_tarefas()


def remover_tarefa():
    print("\n========== REMOVER TAREFA ==========")

    projeto = selecionar_projeto()

    if projeto is None:
        return

    if not projeto.tarefas:
        print("Esse projeto não possui tarefas.")
        return

    projeto.listar_tarefas()

    try:
        indice = int(
            input("\nDigite o número da tarefa: ")
        ) - 1
    except ValueError:
        print("Digite um número válido.")
        return

    tarefa = projeto.remover_tarefa(indice)

    if tarefa:
        print("\nTarefa removida com sucesso!")
    else:
        print("\nTarefa não encontrada.")


def alterar_status():
    print("\n========== ALTERAR STATUS ==========")

    tarefa = selecionar_tarefa()

    if tarefa is None:
        return

    novo_status = escolher_status()

    if novo_status is None:
        print("Status inválido.")
        return

    gerenciador.alterar_status_tarefa(
        tarefa,
        novo_status
    )

    print("\nStatus alterado com sucesso!")


def alterar_prioridade():
    print("\n========== ALTERAR PRIORIDADE ==========")

    tarefa = selecionar_tarefa()

    if tarefa is None:
        return

    nova_prioridade = escolher_prioridade()

    gerenciador.alterar_prioridade_tarefa(
        tarefa,
        nova_prioridade
    )

    print("\nPrioridade alterada com sucesso!")


# ==========================================
# RELATÓRIOS
# ==========================================

def mostrar_progresso():
    print("\n========== PROGRESSO DO PROJETO ==========")

    projeto = selecionar_projeto()

    if projeto is None:
        return

    progresso = projeto.calcular_progresso()

    print(f"\nProjeto: {projeto.nome}")
    print(f"Progresso: {progresso:.2f}%")

    quantidade = int(progresso / 10)

    barra = "█" * quantidade
    barra += "-" * (10 - quantidade)

    print(f"[{barra}]")


def gerar_relatorio_projeto():
    print("\n========== RELATÓRIO DO PROJETO ==========")

    projeto = selecionar_projeto()

    if projeto is None:
        return

    Relatorio.gerar_projeto(projeto)


def gerar_relatorio_geral():
    print("\n========== RELATÓRIO GERAL ==========")

    Relatorio.gerar_geral(gerenciador)


# ==========================================
# MENU PRINCIPAL
# ==========================================

def menu():
    while True:
        print("\n")
        print("=" * 60)
        print("       GERENCIADOR INTELIGENTE DE TAREFAS")
        print("=" * 60)

        print("\n--- USUÁRIOS ---")
        print("1  - Cadastrar usuário")
        print("2  - Listar usuários")
        print("3  - Remover usuário")

        print("\n--- PROJETOS ---")
        print("4  - Criar projeto")
        print("5  - Listar projetos")
        print("6  - Remover projeto")

        print("\n--- TAREFAS ---")
        print("7  - Criar tarefa")
        print("8  - Listar tarefas")
        print("9  - Remover tarefa")
        print("10 - Alterar status")
        print("11 - Alterar prioridade")

        print("\n--- ACOMPANHAMENTO ---")
        print("12 - Ver progresso do projeto")

        print("\n--- RELATÓRIOS ---")
        print("13 - Relatório do projeto")
        print("14 - Relatório geral")

        print("\n0  - Sair")

        opcao = input("\nDigite uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
            pausar()

        elif opcao == "2":
            gerenciador.listar_usuarios()
            pausar()

        elif opcao == "3":
            remover_usuario()
            pausar()

        elif opcao == "4":
            criar_projeto()
            pausar()

        elif opcao == "5":
            listar_projetos()
            pausar()

        elif opcao == "6":
            remover_projeto()
            pausar()

        elif opcao == "7":
            criar_tarefa()
            pausar()

        elif opcao == "8":
            listar_tarefas()
            pausar()

        elif opcao == "9":
            remover_tarefa()
            pausar()

        elif opcao == "10":
            alterar_status()
            pausar()

        elif opcao == "11":
            alterar_prioridade()
            pausar()

        elif opcao == "12":
            mostrar_progresso()
            pausar()

        elif opcao == "13":
            gerar_relatorio_projeto()
            pausar()

        elif opcao == "14":
            gerar_relatorio_geral()
            pausar()

        elif opcao == "0":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    menu()
