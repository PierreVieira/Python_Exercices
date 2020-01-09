ano = int(input('Informe o ano: '))
if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print('Bissexto')
else:
    print('Não bissexto')
