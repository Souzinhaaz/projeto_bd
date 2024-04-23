from connection import ConnectionBD
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

def layout_input_tabela(title, funcionarios, pergunta):
    print(f"{' FUNCIONÁRIOS DA EMPRESA '.center(60, '-')}")
    print(f"\n{title.upper().center(60, '-')}\n")

    id_width, name_width, salary_width = 3, 45, 12

    print(f"{'ID':<{id_width}} {'Nome':<{name_width}} {'Salário':<{salary_width}}")
    print("-" * (id_width + name_width + salary_width))

    for item in funcionarios:
        id, name, salary = item
        print(f"{id:<{id_width}} {name:<{name_width}} {salary:<{salary_width}}")

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

def existe_id(id_funcionario, dados):
    for item in dados:
        if id_funcionario == item[0]:
            return True
    return False

def inserir_no_banco(title, opcao, novo_dado, id):
    con = ConnectionBD("empresa")
    con.criar_tabela()

    try:
        query = f"UPDATE funcionario SET {opcao}=? WHERE id_matricula=?"
        con.crud_operations(query, (novo_dado, id))
        layout_mensagem(title, "Valor editado com sucesso!!!")
    except:
        layout_mensagem(title, "Ocorreu um erro ao editar o dado!!!")


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

        if opcao == "0":
            break
        elif opcao == "1":
            nome = layout_input(title, "Digite o nome do funcionário: ")
            salario = layout_input(title, "Informe o salário do funcionário(opcional): ")
            layout_mensagem(title, "INSERINDO...")

            try:
                con = ConnectionBD("empresa")
                con.criar_tabela()
                query = "INSERT INTO funcionario (nome, salario) VALUES (?, ?)"
                con.crud_operations(query, (nome, salario,))
                layout_mensagem(title, "Valor inserido no banco de dados com sucesso!!!")
            except:
                layout_mensagem(title, "Ocorreu um erro ao inserir os dados no banco de dados!!!")

        else:
            erro = "Insira um valor existente!!!"
            layout_mensagem(title, erro)

        
def editar_funcionario():
    while True:
        limpar()
        title = "Editar Funcionários"
        try:
            con = ConnectionBD("empresa")
            con.criar_tabela()
            funcionarios = con.ordenar("id_matricula")
        except:
            print("Erro ao conectar com o banco de dados!!!")

        id_funcionario = layout_input_tabela(title, funcionarios, "Digite o id do funcionário que deseja editar. \n\n(pressione a tecla 0 para sair!): ")

        if id_funcionario == "0":
            break
        else:
            if existe_id(int(id_funcionario), funcionarios):
                opcao = layout_input(title, "Oque você deseja editar? (nome, salario): ")

                if opcao.lower() == "nome":
                    novo_nome = layout_input(title, "Digite o novo nome: ")
                    layout_mensagem(title, "EDITANDO...")
                    inserir_no_banco(title, opcao, novo_nome, int(id_funcionario))
                elif opcao.lower() == "salario":
                    novo_salario = layout_input(title, "Digite o novo salário: ")
                    layout_mensagem(title, "EDITANDO...")
                    inserir_no_banco(title, opcao, float(novo_salario), int(id_funcionario))
            else:
                layout_mensagem(title, "Não existe o ID no banco de dados")

def excluir_funcionario():
    while True:
        limpar()
        title = "Excluir funcionários"
        try:
            con = ConnectionBD("empresa")
            con.criar_tabela()
            funcionarios = con.ordenar("id_matricula")
        except:
            print("Erro ao conectar com o banco de dados!!!")

        id_funcionario = layout_input_tabela(title, funcionarios, "Digite o id do funcionário que deseja excluir. \n\n(pressione a tecla 0 para sair!): ")

        if id_funcionario == "0":
            break
        else:
            if existe_id(int(id_funcionario), funcionarios):
                try: 
                    layout_mensagem(title, "EXCLUINDO...")
                    query = "DELETE FROM funcionario WHERE id_matricula = ?"
                    con.crud_operations(query, (id_funcionario))
                    layout_mensagem(title, "Valor excluido com sucesso!!!")
                except:
                    layout_mensagem(title, f"Ocorreu um erro ao tentar excluir o funcionário!!!")

            else:
                layout_mensagem(title, "Não existe o ID no banco de dados")

def ordernar_registros():
    while True:
        limpar()
        title = "Ordenar funcionários"
    
        opcao = layout_input(title, "Como você deseja ordernar a tabela? [matricula, nome] \n\n(pressione a tecla 0 para sair!): ")

        if opcao == "0":
            break
        else:
            if opcao.lower() == "matricula" or opcao.lower() == "matrícula":
                try:
                    con = ConnectionBD("empresa")
                    con.criar_tabela()
                    funcionarios = con.ordenar("id_matricula")
                except:
                    print("Erro ao conectar com o banco de dados!!!")

                pergunta = layout_input_tabela(title, funcionarios, "Deseja visualizar a tabela de outra forma?")
                if pergunta[0].upper() == "N":
                    break
            
            elif opcao.lower() == "nome":
                try:
                    con = ConnectionBD("empresa")
                    con.criar_tabela()
                    funcionarios = con.ordenar("nome")
                except:
                    print("Erro ao conectar com o banco de dados!!!")

                pergunta = layout_input_tabela(title, funcionarios, "Deseja visualizar a tabela de outra forma?")
                if pergunta[0].upper() == "N":
                    break
        
def pesquisar_funcionario():
    while True:
        limpar()
        title = "Pesquisar Empregado"

        opcao = layout_input(title, "Como você deseja pesquisar o empregado? [matricula, nome] \n\n(pressione a tecla 0 para sair!): ")

        if opcao == "0":
            break
        else:
            if opcao.lower() == "matricula" or opcao.lower() == "matrícula":
                id = layout_input(title, "Informe o número de matrícula: ")
                
                try:
                    con = ConnectionBD("empresa")
                    con.criar_tabela()
                    funcionarios = con.pesquisar_matricula(id)

                    pergunta = layout_input_tabela(title, funcionarios, "Deseja fazer outra pesquisa? ")
                    if pergunta[0].upper() == "N":
                        break
                except:
                    print("Erro ao conectar com o banco de dados!!!")
            
            elif opcao.lower() == "nome":
                nome = layout_input(title, "Informe o nome: ")

                try:
                    con = ConnectionBD("empresa")
                    con.criar_tabela()
                    funcionarios = con.pesquisar_nome(nome)

                    pergunta = layout_input_tabela(title, funcionarios, "Deseja fazer outra pesquisa? ")
                    if pergunta[0].upper() == "N":
                        break
                except:
                    print("Erro ao conectar com o banco de dados!!!")

def filtrar_funcionario():
    while True:
        limpar()
        title = "Filtrar Funcionários"
        lista_opcoes = [
            "empregados que recebem salários acima de 1000.",
            "empregados que recebem salários abaixo de 1000.",
            "empregados que recebem salários iguais a 1000."
        ]

        opcao = layout(title, lista_opcoes)

        if opcao == "0":
            break
        elif opcao == "1":
            try:
                con = ConnectionBD("empresa")
                con.criar_tabela()
                funcionarios = con.filtrar("acima")

                pergunta = layout_input_tabela(title, funcionarios, "Deseja fazer outro filtro? ")
                if pergunta[0].upper() == "N":
                    break
            except:
                print("Erro ao conectar com o banco de dados!!!")
        elif opcao == "2":
            try:
                con = ConnectionBD("empresa")
                con.criar_tabela()
                funcionarios = con.filtrar("abaixo")

                pergunta = layout_input_tabela(title, funcionarios, "Deseja fazer outro filtro? ")
                if pergunta[0].upper() == "N":
                    break
            except:
                print("Erro ao conectar com o banco de dados!!!")
        elif opcao == "3":
            try:
                con = ConnectionBD("empresa")
                con.criar_tabela()
                funcionarios = con.filtrar("igual")

                pergunta = layout_input_tabela(title, funcionarios, "Deseja fazer outro filtro? ")
                if pergunta[0].upper() == "N":
                    break
            except:
                print("Erro ao conectar com o banco de dados!!!")
