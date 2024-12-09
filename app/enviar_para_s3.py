import boto3

def enviar_para_s3(nome_bucket, nome_arquivo):
    s3 = boto3.client("s3")
    try:
        s3.upload_file(nome_arquivo, nome_bucket, nome_arquivo)
        print(f"Arquivo {nome_arquivo} enviado para o bucket {nome_bucket}.")
    except Exception as erro:
        print(f"Erro ao enviar arquivo: {erro}")

if __name__ == "__main__":
    NOME_BUCKET = "nome-do-seu-bucket"
    NOME_ARQUIVO = "arquivo_aleatorio.txt"
    enviar_para_s3(NOME_BUCKET, NOME_ARQUIVO)
