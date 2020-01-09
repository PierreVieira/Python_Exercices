from datetime import datetime
def bissexto(ano):
    if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False


data = input('Informe mês data e ano separando por espaços: ').split()
dia, mes, ano = map(int, data)
data_valida = True
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
if mes == 2:
    if not bissexto(ano):
        if dia >= 29:
            print('Data inválida, mês de fevereiro tem apenas 28 dias em um ano bissexto!')
            data_valida = False
    if not (1 <= dia <= 28):
        print('Data inválida. Mês de fevereiro só tem do dia 1 ao dia 28.')
        data_valida = False
elif 1 <= mes <= 7:
    if mes % 2 == 0:
        if not (1 <= dia <= 30):
            print(f'Data inválida. Mês de {meses[mes-1]} só tem do dia 1 ao dia 30.')
            data_valida = False
    else:
        if not (1 <= dia <= 31):
            print(f'Data inválida. Mês de {meses[mes-1]} só tem do dia 1 ao dia 31.')
            data_valida = False
elif 8 <= mes <= 12:
    if mes % 2 == 1:
        if not (1 <= dia <= 30):
            print(f'Data inválida. Mês de {meses[mes - 1]} só tem do dia 1 ao dia 30.')
            data_valida = False
    else:
        if not (1 <= dia <= 31):
            print(f'Data inválida. Mês de {meses[mes - 1]} só tem do dia 1 ao dia 31.')
            data_valida = False
else:
    print('Mês digitado é inválido')
    data_valida = False
if data_valida:
    if datetime.now().year < ano:
        print('Data inválida! Ano atual, menor que o ano informado.')
    else:
        print(f'Data registrada: {"/".join(data)}')
