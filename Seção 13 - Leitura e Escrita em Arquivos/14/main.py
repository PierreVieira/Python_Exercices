from datetime import datetime


def calcula_idades():
    string = ''
    for data in tupla_datas:
        diff_dias, diff_meses, diff_anos = atuais['dia'] - data[0], atuais['mes'] - data[1], atuais['ano'] - data[2]
        if diff_meses < 0:
            diff_anos -= 1
        elif diff_dias < 0 and diff_meses == 0:
            diff_anos -= 1
        string += str(diff_anos)+'\n'
    return string


atual = datetime.now()
atuais = {'dia': atual.day, 'mes': atual.month, 'ano': atual.year}
lista_anos = []
with open('nascimento.txt') as arq:
    tupla_strings = tuple(elemento for elemento in arq.read().split('\n'))
    tupla_datas = tuple(tuple(map(int, data.split())) for data in tupla_strings)
string_idades = calcula_idades()
with open('arquivo_idades', 'w') as arq2:
    arq2.write(string_idades)
