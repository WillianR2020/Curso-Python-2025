import logging

# Configuração básica do logging: nível DEBUG e formato com timestamp, nível e mensagem
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='processamento.log')

def processar_dados(dados):
    logging.info("Iniciando o processamento dos dados.")

    if not dados:
        logging.warning("Lista de dados está vazia.")
        return

    for i, item in enumerate(dados):
        logging.debug(f"Processando item {i}: {item}")
        if item < 0:
            logging.error(f"Dado inválido: {item}")

    logging.info("Processamento concluído.")

# Exemplo de uso
dados_exemplo = [10, 5, -2, 8, 0, -5]
processar_dados(dados_exemplo)

print("Os logs foram salvos no arquivo 'processamento.log'")