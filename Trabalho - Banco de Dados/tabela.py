class Tabela:
    def __init__(self):
        import sqlite3
        self.conexao = sqlite3.connect('moleza.sqlite3')
        self.cursor = self.conexao.cursor()
        print('Conexão aberta!')

    # Create table --------------------------------------------------------------------------

    def criar_tabela(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf VARCHAR2(11)
            );
        '''
        self.cursor.execute(sql)
        print('Tabela criada!')

    # Select --------------------------------------------------------------------------

    def selecionar(self):
        sql = '''
            SELECT * FROM pessoas;
        '''
        resultado = self.cursor.execute(sql)
        return resultado.fetchall()

    # Insert --------------------------------------------------------------------------

    def inserir(self, nome, cpf):
        sql = '''
            INSERT INTO pessoas(nome, cpf)
            VALUES (?, ?);
        '''
        self.cursor.execute(sql, [nome, cpf])
        self.conexao.commit()
        print('Inserido!')

    # Update --------------------------------------------------------------------------

    def alterar(self, id, nome, cpf):
        sql = """
            UPDATE pessoas
            SET nome = ?, cpf = ?
            WHERE id = ?;
        """
        self.cursor.execute(sql, [nome, cpf, id])
        self.conexao.commit()
        print('Alterado!')

    # Delete --------------------------------------------------------------------------

    def deletar(self, id):
        sql = """
            DELETE FROM pessoas
            WHERE id = ?;
        """
        self.cursor.execute(sql, [id])
        self.conexao.commit()
        print('Deletado!')

    # Fechar banco de dados -----------------------------------------------------------

    def fechar(self):
        self.conexao.close()
        print('Conexão fechada!')