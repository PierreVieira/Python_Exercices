nome_arquivo = input('Informe o nome do arquivo: ')
caractere = input('Informe o caractere que deseja pesquisar: ')
with open(nome_arquivo) as arq:
    print(f'O caractere {caractere} aparece {arq.read().count(caractere)} vezes no arquivo {nome_arquivo}')