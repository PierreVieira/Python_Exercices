nome_arquivo = input('Informe o nome do arquivo: ')
palavra = input('Informe o palavra que deseja pesquisar: ')
with open(nome_arquivo) as arq:
    print(f'A palavra {palavra.lower()} aparece {arq.read().lower().count(palavra)} vezes no arquivo {nome_arquivo}')
