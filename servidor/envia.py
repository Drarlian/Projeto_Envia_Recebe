"""
Servidor
"""
import socket
from comum.verifica import verifica_arquivo_existe

meu_ip = 'ADICIONAR IP DO SERVIDOR'
minha_porta = 7777

meu_servidor = (meu_ip, minha_porta)

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Esperando conexões...')

servidor.bind(meu_servidor)
servidor.listen(1)

conexao, endereco = servidor.accept()

nome_do_arquivo = verifica_arquivo_existe()

conexao.send(nome_do_arquivo.encode())

with open(nome_do_arquivo, 'rb') as arquivo:
    for dado in arquivo.readlines():
        conexao.send(dado)

print('Arquivo enviado!')
