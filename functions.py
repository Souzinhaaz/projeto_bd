from connection import ConnetionBD
from os import system
from time import sleep

def limpar():
    system('cls')

def layout(title, lista_opcoes):
    print(f"{' FUNCIONÁRIOS DA EMPRESA '.center(60, '-')}")
    print(f"\n{title.upper().center(60, '-')}\n")
    for i, opcao in enumerate(lista_opcoes):
        print(f"{i + 1} - {opcao.upper()}")
    print("0 - SAIR\n")
    print(f"{''.center(60, '-')}")
    
    opcao = input("\nOPCAO: ")
    return opcao

def layout_input(title, pergunta):
    print(f"{' FUNCIONÁRIOS DA EMPRESA '.center(60, '-')}")
    print(f"\n{title.upper().center(60, '-')}\n")

    opcao = input(f"\n{pergunta}")
    return opcao


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
    limpar()
    title = "Cadastrar Funcionários"
    lista_opcoes = [
        "Adicionar dados"
    ]

    opcao = layout(title, lista_opcoes)

    if opcao == "1":
        con = ConnetionBD("empresa")
        limpar()
        pergunta = "Digite o nome do funcionário: "
        nome = layout_input(title, pergunta)
        limpar()
        pergunta = "Informe o salário do funcionário(opcional): "
        salario = layout_input(title, pergunta)

        
    


