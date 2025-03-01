print("Bem vindo ao gerador de senhas")

import random
import string

def gerar_senha(tamanho=20):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Testando a função
tamanho = int(input("Digite o tamanho da senha desejada: "))
print(f"Sua senha gerada é: {gerar_senha(tamanho)}")

pyinstaller --onefile gerador_senhas.py
