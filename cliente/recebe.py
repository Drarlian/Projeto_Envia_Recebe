"""
Cliente
"""
import socket
from time import time
# from comum.calcula import calcula_taxa_transferencia
def calcula_taxa_transferencia(temp_inicial, temp_final, nome_arquivo):
    import os
    tamanho_arquivo = os.path.getsize(f'../cliente/{nome_arquivo}')  # -> +/- 106629 bytes
    # print(f'O tamanho do arquivo é: {tamanho_arquivo} Bytes')

    tamanho_arquivo = tamanho_arquivo / 125000
    print(f'O tamanho do arquivo é {tamanho_arquivo} Megabits')

    tempo_total = temp_final - temp_inicial
    print(f'O tempo total de envio foi: {tempo_total} segundos')

    taxa_transferencia = tamanho_arquivo / tempo_total
    print(f'Taxa de Transferencia: {taxa_transferencia} Mbps')


# ip = 'ADICIONAR IP DO SERVIDOR'
ip = str(input('Digite o ip do servidor: '))
porta = 7777

meu_servidor = (ip, porta)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(meu_servidor)
print('Conectado ao servidor!!\n')

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
