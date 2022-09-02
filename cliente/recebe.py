"""
Cliente
"""
import socket
from time import time
import os

ip = 'ADICIONAR IP DO SERVIDOR'
porta = 7777

meu_servidor = (ip, porta)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(meu_servidor)
print('Conectado!!\n')

nome_do_arquivo = cliente.recv(1024).decode()

with open(nome_do_arquivo, 'wb') as arquivo:
    tempo_inicial = time()
    while True:
        dados = cliente.recv(1_000_000)

        if not dados:
            tempo_final = time()
            break

        arquivo.write(dados)

print(f'{nome_do_arquivo} Recebido!')

tamanho_arquivo = os.path.getsize(nome_do_arquivo)  # -> +/- 106629 bytes
print(f'O tamanho do arquivo é: {tamanho_arquivo} bytes')

tempo_total = tempo_final - tempo_inicial
print(f'O tempo total é: {tempo_total} segundos')

taxa_transferencia = tamanho_arquivo / tempo_total
print(f'Taxa de Transferencia: {taxa_transferencia} b/s')
