from connection import ConnetionBD
from os import system
from time import sleep

def limpar():
    system('cls')

def espera():
    sleep(1.5)

def layout(title, lista_opcoes):
    limpar()
    print(f"{' FUNCIONÁRIOS DA EMPRESA '.center(60, '-')}")
    print(f"\n{title.upper().center(60, '-')}\n")
    for i, opcao in enumerate(lista_opcoes):
        print(f"{i + 1} - {opcao.upper()}")
    print("0 - SAIR\n")
    print(f"{''.center(60, '-')}")
    
    opcao = input("\nOPCAO: ")
    limpar()
    return opcao

def layout_input(title, pergunta):
    limpar()
    print(f"{' FUNCIONÁRIOS DA EMPRESA '.center(60, '-')}")
    print(f"\n{title.upper().center(60, '-')}\n")

    opcao = input(f"\n{pergunta.upper()}")
    limpar()
    return opcao


def layout_mensagem(title, mensagem):
    limpar()
    print(f"{' FUNCIONÁRIOS DA EMPRESA '.center(60, '-')}")
    print(f"\n{title.upper().center(60, '-')}\n")
    print(f"\n{mensagem.upper()}")
    espera()
    limpar()

def menu_opcoes():
    title = "MENU DE OPÇÕES"
    lista_opcoes = [
        "Cadastrar Empregado",
        "Editar Empregado",
        "Excluir Empregado",
        "Ordenar os registros",
        "Pesquisar empregados",
        "Filtrar Empregado"
    ]

    opcao = layout(title, lista_opcoes)
    return opcao

"""
INSERT INTO funcionario (nome, salario) VALUES (?, ?)
DELETE FROM funcionario WHERE id=?
UPDATE funcionario SET nome=?, salario=? WHERE id=?
"""

def cadastrar_funcionario():
    while True:
        limpar()
        title = "Cadastrar Funcionários"
        lista_opcoes = [
            "Adicionar dados"
        ]
        opcao = layout(title, lista_opcoes)

        if opcao == "1":
            con = ConnetionBD("empresa")
            con.criar_tabela()

            pergunta = "Digite o nome do funcionário: "
            nome = layout_input(title, pergunta)
            pergunta = "Informe o salário do funcionário(opcional): "
            salario = layout_input(title, pergunta)

            layout_mensagem(title, "INSERINDO...")

            try:
                query = "INSERT INTO funcionario (nome, salario) VALUES (?, ?)"
                con.crud_operations(query, (nome, salario,))
                layout_mensagem(title, "Valor inserido no banco de dados com sucesso!!!")
            except:
                layout_mensagem(title, "Ocorreu um erro ao inserir os dados no banco de dados!!!")
        else:
            erro = "Insira um valor existente!!!"
            layout_mensagem(title, erro)

        
    


