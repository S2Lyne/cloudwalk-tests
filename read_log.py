# read_log.py
import os

def read_log_file(log_file_path):
    """
    Função para ler o arquivo de log do Quake e extrair as informações necessárias.

    Args:
    log_file_path (str): O caminho para o arquivo de log.

    Returns:
    list: Uma lista de strings contendo as linhas do arquivo de log.
    """
    if not os.path.exists(log_file_path):
        raise FileNotFoundError(f"O arquivo {log_file_path} não foi encontrado.")

    with open(log_file_path, 'r') as file:
        log_data = file.readlines()
    return log_data
