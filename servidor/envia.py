"""
Servidor
"""
import socket
# from comum.verifica import verifica_arquivo_existe
def verifica_arquivo_existe():
    while True:
        nome_arquivo = str(input('Digite o nome do arquivo a ser enviado: '))

        try:
            open(nome_arquivo, 'r').close()
        except FileNotFoundError:
            print('O arquivo informado não existe!')
        else:
            print('Achei!')
            return nome_arquivo


meu_ip = ''
minha_porta = 7777

meu_servidor = (meu_ip, minha_porta)

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Esperando conexões...')

servidor.bind(meu_servidor)
servidor.listen(1)

conexao, endereco = servidor.accept()

print('Conectado ao cliente!!\n')

nome_do_arquivo = verifica_arquivo_existe()

conexao.send(nome_do_arquivo.encode())

with open(nome_do_arquivo, 'rb') as arquivo:
    for dado in arquivo.readlines():
        conexao.send(dado)

print('Arquivo enviado!')
