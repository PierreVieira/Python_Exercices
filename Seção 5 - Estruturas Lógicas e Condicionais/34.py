nota = float(input('Informe a nota do aluno: '))
faltas = int(input('Informe a quantidade de faltas do aluno: '))
if faltas <= 20:
    if nota <= 3.9:
        print('E')
    elif nota <= 4.9:
        print('D')
    elif nota <= 7.4:
        print('C')
    elif nota <= 8.9:
        print('B')
    else:
        print('A')
else:
    if nota <= 3.9:
        print('E')
    elif nota <= 4.9:
        print('E')
    elif nota <= 7.4:
        print('D')
    elif nota <= 8.9:
        print('C')
    else:
        print('B')
