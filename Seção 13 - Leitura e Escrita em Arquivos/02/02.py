nome_arquivo = input('Informe o nome do arquivo: ')
with open(nome_arquivo) as arq:
    print(f'O arquivo {nome_arquivo} tem {len(arq.readlines())} linhas.')
