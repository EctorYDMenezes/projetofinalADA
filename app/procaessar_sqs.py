import boto3

def processar_mensagens_sqs(url_fila):
    sqs = boto3.client("sqs")
    while True:
        mensagens = sqs.receive_message(
            QueueUrl=url_fila, MaxNumberOfMessages=10, WaitTimeSeconds=10
        )
        if "Messages" in mensagens:
            for mensagem in mensagens["Messages"]:
                corpo = mensagem["Body"]
                print(f"Processando mensagem: {corpo}")
                # Aqui você pode incluir lógica para salvar no banco de dados
                sqs.delete_message(QueueUrl=url_fila, ReceiptHandle=mensagem["ReceiptHandle"])

if __name__ == "__main__":
    URL_FILA = "url-da-sua-fila-sqs"
    processar_mensagens_sqs(URL_FILA)
