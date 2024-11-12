# Importações: 
import conexao
from tkinter import messagebox

'''BACK-END: MANIPULAÇÃO DE DADOS (CRUD) NO BANCO DE DADOS.'''

# Inserir despesa no banco.
def inserir_despesa(valor, categoria, data, descricao):
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO despesas (valor, categoria, data, descricao)
            VALUES (%s, %s, %s, %s)
        """, (valor, categoria, data, descricao))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Despesa adicionada com sucesso!")

# Exibir todas as despesas existentes no banco.
def listar_despesas():
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM despesas")
        despesas = cursor.fetchall()
        conn.close()
        return despesas
    return []

# Deletar despesa.
def remover_despesa(despesa_id):
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM despesas WHERE id = %s", (despesa_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Despesa removida com sucesso!")


# Atualizar despesa preexistente.
def atualizar_despesa(despesa_id, valor, categoria, data, descricao):
    conn = conexao.conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE despesas 
            SET valor = %s, categoria = %s, data = %s, descricao = %s
            WHERE id = %s
        """, (valor, categoria, data, descricao, despesa_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Despesa atualizada com sucesso!")