import functions

while True:
    functions.limpar()
    parametro = functions.menu_opcoes()
    functions.limpar()

    if parametro == "1":
        functions.cadastrar_funcionario()
    elif parametro == "2":
        functions.editar_funcionario()
    elif parametro == "3":
        functions.excluir_funcionario()
    elif parametro == "4":
        functions.ordernar_registros()
    elif parametro == "5":
        functions.pesquisar_funcionario()
    elif parametro == "6":
        functions.filtrar_funcionario() 
    elif parametro == "0":
        print("Fim do programa!!!")
        break