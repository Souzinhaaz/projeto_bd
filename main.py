import functions

while True:
    functions.limpar()
    parametro = functions.menu_opcoes()
    functions.limpar()

    if parametro == "1":
        functions.cadastrar_funcionario()
    elif parametro == "0":
        print("Fim do programa!!!")
        break