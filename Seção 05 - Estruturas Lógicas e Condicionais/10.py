sexo = input('Informe o seu sexo [M/F]: ')
altura = float(input('Informe sua altura em metros: '))
print('Peso ideal: ', end='')
if sexo.upper() == 'M':
    print(f'{72*altura - 58:.2f}')
else:
    print(f'{62.1*altura - 44.7:.2f}')
