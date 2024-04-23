import sqlite3

class ConnectionBD():
    def __init__(self, nome_arquivo):
        self.nome_bd = nome_arquivo
        self.conectar()
        self.conexao.close()
        self.criar_tabela()

    def conectar(self):
        self.conexao = sqlite3.connect(f"{self.nome_bd}.db")
        self.cursor = self.conexao.cursor()

    def criar_tabela(self):
        self.conectar()
        query = '''
            CREATE TABLE IF NOT EXISTS funcionario (
                id_matricula INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(45) NOT NULL,
                salario FLOAT NOT NULL
            )
        '''
        self.cursor.execute(query)
        self.conexao.close()

    def crud_operations(self, query, dados=None):
        self.conectar()
        if dados:
            self.cursor.execute(query, dados)
        else:
            self.cursor.execute(query)
        self.conexao.commit()
        self.conexao.close()

    def ordenar(self, order_column):
        self.conectar()
        query = f'''
            SELECT id_matricula, nome, salario FROM funcionario ORDER BY {order_column}
        '''
        self.cursor.execute(query)
        funcionarios = self.cursor.fetchall()
        self.conexao.close()

        return funcionarios
    
    def pesquisar_matricula(self, search):
        self.conectar()
        query = f'''
            SELECT id_matricula, nome, salario FROM funcionario WHERE id_matricula = ?
        '''
        self.cursor.execute(query, (search,))
        funcionarios = self.cursor.fetchall()
        self.conexao.close()

        return funcionarios
    
    def pesquisar_nome(self, search):
        self.conectar()
        query = f'''
            SELECT id_matricula, nome, salario FROM funcionario WHERE nome = ?
        '''
        self.cursor.execute(query, (search,))
        funcionarios = self.cursor.fetchall()
        self.conexao.close()

        return funcionarios
        
    def filtrar(self, condition):
        self.conectar()
        if condition == "acima":
            query = '''
                SELECT id_matricula, nome, salario FROM funcionario WHERE salario > 1000
            '''
        elif condition == "abaixo":
            query = '''
                SELECT id_matricula, nome, salario FROM funcionario WHERE salario < 1000
            '''
        elif condition == "igual":
            query = '''
                SELECT id_matricula, nome, salario FROM funcionario WHERE salario == 1000
            '''
        self.cursor.execute(query)
        funcionarios = self.cursor.fetchall()
        self.conexao.close()

        return funcionarios
    
