import tkinter as tk
from tkinter import messagebox

saldo = 0
extrato = ""
nsaques = 0
Lsaque = 500
Lsaques = 3

def realizar_operacao(opcao):
    global saldo, extrato, nsaques
    
    if opcao == 1:  # Depositar
        valor = float(entrada_valor.get())
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            messagebox.showinfo("Informação", f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Valor inválido")
    
    elif opcao == 2:  # Sacar
        valor = float(entrada_valor.get())
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > Lsaque
        excedeu_saques = nsaques >= Lsaques

        if excedeu_saldo:
            messagebox.showerror("Erro", "Saldo insuficiente.")
        elif excedeu_saques:
            messagebox.showerror("Erro", f"Você excedeu o limite de {Lsaques} saques hoje.")
        elif excedeu_limite:
            messagebox.showerror("Erro", f"Você excedeu o limite de R${Lsaque}.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            nsaques += 1
            messagebox.showinfo("Informação", f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Valor inválido")

    elif opcao == 3:  # Extrato
        messagebox.showinfo("Extrato", f"Extrato:\n{extrato}\nSaldo: R$ {saldo:.2f}")
    
    elif opcao == 0:  # Sair
        janela.quit()

def enviar_nome():
    nome = entrada_nome.get()
    messagebox.showinfo("Informação", f"Olá, {nome}!")
    label_opcoes.pack()
    entrada_valor.pack()
    botao_depositar.pack()
    botao_sacar.pack()
    botao_extrato.pack()
    botao_sair.pack()

# Criar a janela principal
janela = tk.Tk()
janela.title("NãoBank")
janela.configure(bg="#d7ffd9")  # Cor de fundo verde claro

# Criar e posicionar os widgets iniciais
titulo = tk.Label(janela, text="Bem-vindo ao NãoBank", font=("Arial", 16, "bold"), bg="#d7ffd9", fg="#333333")
titulo.pack(pady=10)

label_nome = tk.Label(janela, text="Digite seu nome:", font=("Arial", 12), bg="#d7ffd9", fg="#333333")
label_nome.pack()

entrada_nome = tk.Entry(janela, font=("Arial", 12))
entrada_nome.pack(pady=5)

botao_enviar = tk.Button(janela, text="Enviar", command=enviar_nome, font=("Arial", 12), bg="#007bff", fg="#ffffff", width=10)
botao_enviar.pack(pady=10)

# Widgets para operações bancárias
label_opcoes = tk.Label(janela, text="Escolha uma opção:", font=("Arial", 12), bg="#d7ffd9", fg="#333333")
entrada_valor = tk.Entry(janela, font=("Arial", 12))
botao_depositar = tk.Button(janela, text="Depositar", command=lambda: realizar_operacao(1), font=("Arial", 12), bg="#007bff", fg="#ffffff", width=10)
botao_sacar = tk.Button(janela, text="Sacar", command=lambda: realizar_operacao(2), font=("Arial", 12), bg="#007bff", fg="#ffffff", width=10)
botao_extrato = tk.Button(janela, text="Extrato", command=lambda: realizar_operacao(3), font=("Arial", 12), bg="#007bff", fg="#ffffff", width=10)
botao_sair = tk.Button(janela, text="Sair", command=lambda: realizar_operacao(0), font=("Arial", 12), bg="#007bff", fg="#ffffff", width=10)

# Iniciar o loop principal
janela.mainloop()
