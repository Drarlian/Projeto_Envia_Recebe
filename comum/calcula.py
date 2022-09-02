def calcula_taxa_transferencia(temp_inicial, temp_final, nome_arquivo):
    import os
    tamanho_arquivo = os.path.getsize(f'../cliente/{nome_arquivo}')  # -> +/- 106629 bytes
    print(f'O tamanho do arquivo é: {tamanho_arquivo} Bytes')

    tempo_total = temp_final - temp_inicial
    print(f'O tempo total é: {tempo_total} segundos')

    taxa_transferencia = tamanho_arquivo / tempo_total
    print(f'Taxa de Transferencia: {taxa_transferencia} B/s')
