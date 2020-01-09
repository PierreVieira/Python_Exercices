def trocar_minusculas_por_maiusculas(string):
    palavras = string.split('\n')
    palavras = [palavra.upper() for palavra in palavras]
    with open(nome_arquivo_saida, 'w') as arq2:
        arq2.write('\n'.join(palavras))


nome_arquivo = input('Informe o nome do arquivo de origem: ')
nome_arquivo_saida = input('Infrome o nome do arquivo de saída: ')
with open(nome_arquivo) as arq:
    trocar_minusculas_por_maiusculas(arq.read())
