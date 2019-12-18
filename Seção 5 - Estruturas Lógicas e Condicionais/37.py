def primeira_faixa(horario1, horario2):
    if horario1[0] > horario2[0]:
        return [False] #O valor não está na primeira faixa
    elif horario1[0] == horario2[0]:
        return [True, 1] #O valor está na primeira faixa
    elif horario2[0] - horario1[0] == 1:#horario1[0] < horario2[0]
        return [True, 1]
    elif horario2[0] - horario1[0] == 2:
        return [True, 2]
    else:
        return [False] #O valor não está na primeira faixa


def segunda_faixa(horario1, horario2):
    if horario1[0] > horario2[0]:
        return [False]  # O valor não está na segunda faixa
    elif horario1[0] == horario2[0]:
        return [True, 1]  # O valor está na segunda faixa
    elif horario2[0] - horario1[0] == 3:  # horario1[0] < horario2[0]
        return [True, 3*1.4]
    elif horario2[0] - horario1[0] == 4:
        return [True, 4*1.4]
    else:
        return [False]  # O valor não está na segunda faixa



h1, m1, s1 = map(int, input('Informe o horário de chegada separando por espaços: ').split())
h2, m2, s2 = map(int, input('Informe o horário de partida separando por espaços: ').split())
if not(0 <= h1 <= 23):
    print('O horário de chegada apresenta erro nas horas.')
elif not (0 <= m1 <= 59):
    print('O horário de chegada apresenta erro nos minutos.')
elif not (0 <= s1 <= 59):
    print('O horário de chegada apresenta erro nos segundos.')
elif not(0 <= h2 <= 23):
    print('O horário de partida apresenta erro nas horas.')
elif not (0 <= m2 <= 59):
    print('O horário de partida apresenta erro nos minutos.')
elif not (0 <= s2 <= 59):
    print('O horário de partida apresenta erro nos segundos.')
else:
    retorno1 = primeira_faixa([h1, m1, s1], [h2, m2, s2])
    retorno2 = segunda_faixa([h1, m1, s1], [h2, m2, s2])
    print('Você pagará: R$ ', end='')
    if retorno1[0]:
        print(f'{retorno1[1]:.2f}')
    elif retorno2[0]:
        print(f'{retorno2[1]:.2f}')
    else: #terceira faixa
        if h2 >= h1:
            if m2 >= m1:
                if s2 >= s1:
                    print(f'{2*(h1-h2):.2f}')
                else: #s2 < s1
                    print(f'{2*(h1-h2)-1:.2f}')
            else: #m2 < m1
                print(f'{2*(h1-h2)-1:.2f}')
        else: #h2 <= h1
            if m2 >= m1:
                if s2 >= s1:
                    print(f'{2 * (24 - h2 - h1):.2f}')
                else:  # s2 < s1
                    print(f'{2 * (24 - h2 - h1) - 1:.2f}')
            else:  # m2 < m1
                print(f'{2 * (24 - h2 - h1) - 1:.2f}')
