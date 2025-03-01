import tkinter as tk
from tkinter import messagebox
import random
import string

# Função para gerar senha personalizada
def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        incluir_maiusculas = var_maiusculas.get()
        incluir_minusculas = var_minusculas.get()
        incluir_numeros = var_numeros.get()
        incluir_especiais = var_especiais.get()

        caracteres = ''
        if incluir_maiusculas:
            caracteres += string.ascii_uppercase
        if incluir_minusculas:
            caracteres += string.ascii_lowercase
        if incluir_numeros:
            caracteres += string.digits
        if incluir_especiais:
            caracteres += string.punctuation

        if not caracteres:
            raise ValueError("Selecione pelo menos um tipo de caractere.")

        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        label_resultado.config(text=f"Senha Gerada: {senha}")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Configuração da janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")

# Tamanho da senha
label_tamanho = tk.Label(janela, text="Tamanho da senha:")
label_tamanho.pack(pady=5)

entry_tamanho = tk.Entry(janela)
entry_tamanho.pack(pady=5)

# Opções de personalização
var_maiusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_especiais = tk.BooleanVar(value=True)

chk_maiusculas = tk.Checkbutton(janela, text="Incluir Letras Maiúsculas", variable=var_maiusculas)
chk_maiusculas.pack()

chk_minusculas = tk.Checkbutton(janela, text="Incluir Letras Minúsculas", variable=var_minusculas)
chk_minusculas.pack()

chk_numeros = tk.Checkbutton(janela, text="Incluir Números", variable=var_numeros)
chk_numeros.pack()

chk_especiais = tk.Checkbutton(janela, text="Incluir Caracteres Especiais", variable=var_especiais)
chk_especiais.pack()

# Botão para gerar senha
btn_gerar = tk.Button(janela, text="Gerar Senha", command=gerar_senha)
btn_gerar.pack(pady=10)

# Resultado
label_resultado = tk.Label(janela, text="Sua senha aparecerá aqui.")
label_resultado.pack(pady=10)

# Inicia o loop da interface gráfica
janela.mainloop()
