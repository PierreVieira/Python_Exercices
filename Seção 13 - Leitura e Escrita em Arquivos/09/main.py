nome_arquivo1 = input('Informe o nome do primeiro arquivo: ')
nome_arquivo2 = input('Informe o nome do segundo arquivo: ')
nome_arquivo3 = 'arq3.txt'
with open(nome_arquivo1) as arq1:
    string = arq1.read()
string += '\n\n'
with open(nome_arquivo2) as arq2:
    string += arq2.read()
with open(nome_arquivo3, 'a') as arq3:
    arq3.write(string)
