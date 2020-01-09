def conta(string):
    qtde = 0
    for caractere in string:
        arq.seek(0)
        qtde += arq.read().upper().count(caractere)
    return qtde

nome_arquivo = input('Informe o nome do arquivo: ')
vogais = 'AEIOU'
consoantes = 'BCDFGHJKLMNPQRSTVWXYZ'
with open(nome_arquivo) as arq:
    qtde_vogais = conta(vogais)
    qtde_consoantes = conta(consoantes)
    print(f'O arquivo {nome_arquivo} tem\n{qtde_vogais} vogais.\n{qtde_consoantes} consoantes.')