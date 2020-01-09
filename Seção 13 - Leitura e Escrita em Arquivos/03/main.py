nome_arquivo = input('Informe o nome do arquivo: ')
vogais = 'AEIOU'
qtde_vogais = 0
with open(nome_arquivo) as arq:
    for v in vogais:
        arq.seek(0)
        qtde_vogais += arq.read().upper().count(v)
    print(f'O arquivo {nome_arquivo} tem {qtde_vogais} vogais')