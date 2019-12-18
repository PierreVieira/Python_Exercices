a, b = map(int, input('Informe dois números inteiros: ').split())
if a > b:
    print(f'Maior: {a}')
elif b > a:
    print(f'Maior: {b}')
else:
    print('Números iguais')
