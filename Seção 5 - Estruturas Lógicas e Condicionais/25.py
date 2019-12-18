a, b, c = map(float, input('Informe os coeficientes da equação de segundo grau: ').split())
if a == 0:
    print('Uma equação de segundo grau não pode ter o coeficiente A = 0')
else:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print('Não admite raízes reais')
        print(f'Raízes complexas:\n{(-b+delta**0.5)/2*a:.2f}\n{(-b-delta**0.5)/2*a:.2f}')
    elif delta == 0:
        print(f'Raíz única: {-b/2*a:.2f}')
    else:
        print(f'Duas raízes possíveis:\n{(-b+delta**0.5)/2*a:.2f}\n{(-b-delta**0.5)/2*a:.2f}')
