def gerar_matriz():
    matriz = []
    for c in range(qtde_linhas):
        matriz.append([])
    for c in range(qtde_linhas):
        for d in range(qtde_colunas):
            if (c, d) not in anuladas_tuple:
                matriz[c].append(1)
            else:
                matriz[c].append(0)
    return matriz


def gerar_segundo_arquivo():
    string_arquivo = ''
    for c in matriz:
        for d in c:
            string_arquivo += str(d)+' '
        string_arquivo = string_arquivo.strip()
        string_arquivo += '\n'
    with open('saida.txt', 'w') as arq2:
        arq2.write(string_arquivo[:-1:])


with open('matriz_info.txt') as arq:
    qtde_linhas, qtde_colunas, qtde_anuladas = map(int, arq.readline().strip('\n').split())
    anuladas_string = tuple(map(lambda string: tuple(string.split()), arq.read().split('\n')))
    anuladas_tuple = tuple(map(lambda tupla: (int(tupla[0]), int(tupla[1])), anuladas_string))
matriz = gerar_matriz()
gerar_segundo_arquivo()
