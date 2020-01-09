from random import sample
lista_inteiros = sorted(sample(range(1, 100), 10))
lista_binarios = list(map(lambda numero: bin(numero).replace('0b', ''), lista_inteiros))
with open('saida.txt', 'w') as arq:
    arq.write('\n'.join(lista_binarios))
