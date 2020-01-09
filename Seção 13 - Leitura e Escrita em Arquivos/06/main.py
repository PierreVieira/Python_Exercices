def qtde_aparicoes(letra, string):
    qtde_ap = string.count(letra.upper()) + string.count(letra.lower())
    return qtde_ap


nome_arquivo = input('Informe o nome do arquivo: ')
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open(nome_arquivo) as arq:
    for letra in letras:
        arq.seek(0)
        print(f'A letra {letra} aparece {qtde_aparicoes(letra, arq.read())} vezes no arquivo {nome_arquivo}.')
