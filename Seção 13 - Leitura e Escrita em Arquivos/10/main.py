from collections import Counter
with open('entrada.txt') as entrada:
    tuplas_pessoas = tuple(tuple(pessoa.split(';')) for pessoa in entrada.read().split('\n'))  # 0: nome; 1: cidade
lista_cidades = Counter([cidade[1] for cidade in tuplas_pessoas])
cidade_mais_populosa = lista_cidades.most_common(1)
saida_string = f'A cidade mais populosa é {cidade_mais_populosa[0][0]} com {cidade_mais_populosa[0][1]} habitantes.'
with open('saida.txt', 'w', encoding='utf-8') as saida:
    saida.write(saida_string)
