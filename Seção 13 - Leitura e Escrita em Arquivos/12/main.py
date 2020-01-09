def printa(lista):
    for elemento in lista:
        print(f'A letra {elemento[0]} aparece {elemento[1]} vezes no arquivo.')


nome_arquivo = input('Informe o nome do arquivo: ')
with open(nome_arquivo) as arq:
    conteudo = arq.read().strip('\n')
    arq.seek(0)
    numero_linhas = len(arq.readlines())
    lista_palavras = conteudo.split()
    qtde_palavras = len(lista_palavras)
    qtde_cada_letra = [(letra.upper(), conteudo.upper().count(letra.upper())) for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
print(f'Número de linhas: {numero_linhas}')
print(f'Número de palavras: {qtde_palavras}')
printa(qtde_cada_letra)
