import tkinter as tk
from tkinter import messagebox
import sqlite3

class UsuarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Usuários")
        self.root.geometry("500x420") 

        self.conn = sqlite3.connect('usuarios.db')
        self.cursor = self.conn.cursor()
        self.create_table()

        self.nome_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.idade_var = tk.StringVar()

        tk.Label(root, text="Nome").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.nome_var, width=40).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.email_var, width=40).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(root, text="Idade").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.idade_var, width=40).grid(row=2, column=1, padx=10, pady=10)

        tk.Button(root, text="Adicionar", command=self.adicionar_usuario).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(root, text="Atualizar", command=self.atualizar_usuario).grid(row=3, column=1, padx=10, pady=10)
        tk.Button(root, text="Deletar", command=self.deletar_usuario).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(root, text="Listar", command=self.listar_usuarios).grid(row=4, column=1, padx=10, pady=10)

        self.lista_usuarios = tk.Listbox(root, width=80)  # Aumentei a largura do Listbox
        self.lista_usuarios.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        self.lista_usuarios.bind('<<ListboxSelect>>', self.selecionar_usuario)

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER PRIMARY KEY,
                                nome TEXT,
                                email TEXT,
                                idade INTEGER)''')
        self.conn.commit()

    def adicionar_usuario(self):
        nome = self.nome_var.get()
        email = self.email_var.get()
        idade = self.idade_var.get()
        if nome and email and idade:
            self.cursor.execute("INSERT INTO usuarios (nome, email, idade) VALUES (?, ?, ?)", (nome, email, idade))
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso")
            self.listar_usuarios()
        else:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios")

    def atualizar_usuario(self):
        try:
            selected_item = self.lista_usuarios.curselection()[0]
            user_id = self.lista_usuarios.get(selected_item).split()[0]
            nome = self.nome_var.get()
            email = self.email_var.get()
            idade = self.idade_var.get()
            if nome and email and idade:
                self.cursor.execute("UPDATE usuarios SET nome=?, email=?, idade=? WHERE id=?", (nome, email, idade, user_id))
                self.conn.commit()
                messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso")
                self.listar_usuarios()
            else:
                messagebox.showwarning("Atenção", "Todos os campos são obrigatórios")
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um usuário para atualizar")

    def deletar_usuario(self):
        try:
            selected_item = self.lista_usuarios.curselection()[0]
            user_id = self.lista_usuarios.get(selected_item).split()[0]
            self.cursor.execute("DELETE FROM usuarios WHERE id=?", (user_id,))
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Usuário deletado com sucesso")
            self.listar_usuarios()
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um usuário para deletar")

    def listar_usuarios(self):
        self.lista_usuarios.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM usuarios")
        for row in self.cursor.fetchall():
            self.lista_usuarios.insert(tk.END, f"{row[0]} - Nome: {row[1]}, Email: {row[2]}, Idade: {row[3]}")

    def selecionar_usuario(self, event):
        try:
            selected_item = self.lista_usuarios.curselection()[0]
            user_data = self.lista_usuarios.get(selected_item).split(" - ")
            user_id, user_info = user_data[0], user_data[1]
            nome, email, idade = user_info.split(", ")
            self.nome_var.set(nome.split(": ")[1])
            self.email_var.set(email.split(": ")[1])
            self.idade_var.set(idade.split(": ")[1])
        except IndexError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = UsuarioApp(root)
    root.mainloop()