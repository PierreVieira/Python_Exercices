altura = float(input('Informe sua altura em metros: '))
peso = float(input('Informe seu peso em quilogramas: '))
if altura < 1.2:
    if peso <= 60:
        print('A')
    elif peso <= 90:
        print('D')
    else:
        print('G')
elif altura <= 1.7:
    if peso <= 60:
        print('B')
    elif peso <= 90:
        print('E')
    else:
        print('H')
else:
    if peso <= 60:
        print('C')
    elif peso <= 90:
        print('F')
    else:
        print('I')
