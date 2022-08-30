"""
Cliente
"""
import socket

ip = 'ADICIONAR IP DO SERVIDOR'
porta = 7777

meu_servidor = (ip, porta)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(meu_servidor)
print('Conectado!!\n')

nome_do_arquivo = cliente.recv(1024).decode()

with open(nome_do_arquivo, 'wb') as arquivo:
    while True:
        dados = cliente.recv(1_000_000)

        if not dados:
            break

        arquivo.write(dados)

print(f'{nome_do_arquivo} Recebido!')
