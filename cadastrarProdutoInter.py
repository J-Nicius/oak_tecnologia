import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

produtos = []


def cadastrar_produto():

    def salvar_produto():
        nome = nome_entry.get()
        descricao = descricao_entry.get()
        try:
            valor = float(valor_entry.get())
            if valor < 0:
                messagebox.showerror("Erro", "O valor não pode ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido. Digite um número.")
            return
        disponivel = "sim" if disponivel_var.get() == 1 else "não"
        produtos.append(
            {
                "nome": nome,
                "descricao": descricao,
                "valor": valor,
                "disponivel": disponivel,
            }
        )
        janela_cadastro.destroy()
        atualizar_listagem()

    janela_cadastro = tk.Toplevel(janela)
    janela_cadastro.title("Cadastrar Produto")

    tk.Label(janela_cadastro, text="Nome:").grid(row=0, column=0, sticky=tk.W)
    nome_entry = tk.Entry(janela_cadastro)
    nome_entry.grid(row=0, column=1)

    tk.Label(janela_cadastro, text="Descrição:").grid(row=1, column=0, sticky=tk.W)
    descricao_entry = tk.Entry(janela_cadastro)
    descricao_entry.grid(row=1, column=1)

    tk.Label(janela_cadastro, text="Valor:").grid(row=2, column=0, sticky=tk.W)
    valor_entry = tk.Entry(janela_cadastro)
    valor_entry.grid(row=2, column=1)

    disponivel_var = tk.IntVar()
    tk.Checkbutton(janela_cadastro, text="Disponível", variable=disponivel_var).grid(
        row=3, column=0, columnspan=2
    )

    tk.Button(janela_cadastro, text="Salvar", command=salvar_produto).grid(
        row=4, column=0, columnspan=2
    )


def atualizar_listagem():

    for item in tree.get_children():
        tree.delete(item)

    produtos_ordenados = sorted(produtos, key=lambda produto: produto["valor"])
    for produto in produtos_ordenados:
        tree.insert("", tk.END, values=(produto["nome"], f"{produto['valor']:.2f}"))


janela = tk.Tk()
janela.title("Cadastro de Produtos")

tree = ttk.Treeview(janela, columns=("Nome", "Valor"), show="headings")
tree.heading("Nome", text="Nome")
tree.heading("Valor", text="Valor")
tree.pack(pady=10)

botao_cadastrar = tk.Button(janela, text="Cadastrar Produto", command=cadastrar_produto)
botao_cadastrar.pack()

atualizar_listagem()

janela.mainloop()
