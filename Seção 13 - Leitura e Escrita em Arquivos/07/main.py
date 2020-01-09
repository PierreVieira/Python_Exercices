def trocar_vogais_por_asterisco(string):
    palavras = string.split('\n')
    for v in vogais:
        palavras = [palavra.replace(v.upper(), '*') for palavra in palavras]
        palavras = [palavra.replace(v.lower(), '*') for palavra in palavras]
    with open(nome_arquivo_saida, 'w') as arq2:
        arq2.write('\n'.join(palavras))


nome_arquivo = input('Informe o nome do arquivo de origem: ')
nome_arquivo_saida = input('Infrome o nome do arquivo de saída: ')
vogais = 'AEIOU'
with open(nome_arquivo) as arq:
    trocar_vogais_por_asterisco(arq.read())
