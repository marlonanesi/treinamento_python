import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS veiculos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                marca TEXT,
                modelo TEXT,
                ano INTEGER,
                tipo TEXT
            )
        ''')
        self.connection.commit()

    def inserir_veiculo(self, marca, modelo, ano, tipo):
        self.cursor.execute('''
            INSERT INTO veiculos (marca, modelo, ano, tipo)
            VALUES (?, ?, ?, ?)
        ''', (marca, modelo, ano, tipo))
        self.connection.commit()

    def listar_veiculos(self):
        self.cursor.execute('SELECT * FROM veiculos')
        return self.cursor.fetchall()

    def atualizar_veiculo(self, veiculo_id, marca, modelo, ano, tipo):
        self.cursor.execute('''
            UPDATE veiculos
            SET marca = ?, modelo = ?, ano = ?, tipo = ?
            WHERE id = ?
        ''', (marca, modelo, ano, tipo, veiculo_id))
        self.connection.commit()

    def remover_veiculo(self, veiculo_id):
        self.cursor.execute('DELETE FROM veiculos WHERE id = ?', (veiculo_id,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()