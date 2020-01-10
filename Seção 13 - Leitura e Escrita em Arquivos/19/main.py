with open('arq.txt', encoding='utf-8') as arq:
    lista_nomes = []
    lista_notas = []
    for linha in arq.read().split('\n'):
        lista_notas.append(int(linha[linha.rfind(':')+1:]))
        lista_nomes.append(linha[linha.find(':')+1:linha.find(' ')])
maior_nota = max(lista_notas)
lista_melhores_name = [lista_nomes[i] for i in range(len(lista_nomes)) if lista_notas[i] == maior_nota]
print('Os melhores alunos foram:')
for name in lista_melhores_name:
    print(f"\033[0;32m{name.center(len('Os melhores alunos foram:'))}\033[m")
print(f'Com nota de', end=' ')
print(f'\033[1;34m{maior_nota}\033[m')
