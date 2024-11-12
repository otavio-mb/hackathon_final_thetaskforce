# Importações: 
import mysql.connector
from tkinter import messagebox

'''BACK-END: CONFIGURAÇÃO E CONEXÃO COM O BANCO DE DADOS'''

# Dados de configuração para a conexão.
DB_CONFIG = {
    'host': "localhost",
    'user': "thetaskforce",
    'password': "12345678",
    'database': "projeto_crud"
}

# Conectar com o banco de dados.
def conectar():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Erro de Conexão", f"Erro ao conectar ao banco de dados: {err}")
        return None

# Criar tabela de despesas (caso não exista).
def criar_tabelas():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS despesas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                valor DECIMAL(10, 2) NOT NULL,
                categoria VARCHAR(50) NOT NULL,
                data DATE NOT NULL,
                descricao VARCHAR(255)
            )
        """)
        conn.commit()
        conn.close()