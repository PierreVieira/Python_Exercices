from datetime import datetime
ano_atual = datetime.now().year
with open('entrada.txt') as arq:
    tupla_nascimentos = tuple(int(string[string.find(';')+1::]) for string in arq.readlines())
with open('saida.txt', 'w') as arq2:
    for ano_nascimento in tupla_nascimentos:
        arq2.write(str(ano_atual - ano_nascimento)+'\n')