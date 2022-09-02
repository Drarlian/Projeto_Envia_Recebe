"""
Cliente
"""
import socket
from time import time
from comum.calcula import calcula_taxa_transferencia

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

calcula_taxa_transferencia(tempo_inicial, tempo_final, nome_do_arquivo)
