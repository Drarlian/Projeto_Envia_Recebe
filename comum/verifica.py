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
