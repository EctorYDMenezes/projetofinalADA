import random

def gerar_arquivo_aleatorio():
    numero_linhas = random.randint(1, 100)  # Número aleatório de linhas
    nome_arquivo = "arquivo_aleatorio.txt"
    with open(nome_arquivo, "w") as arquivo:
        for i in range(numero_linhas):
            arquivo.write(f"Linha {i+1}\n")
    return nome_arquivo, numero_linhas

if __name__ == "__main__":
    nome_arquivo, quantidade_linhas = gerar_arquivo_aleatorio()
    print(f"Arquivo gerado: {nome_arquivo} com {quantidade_linhas} linhas.")
