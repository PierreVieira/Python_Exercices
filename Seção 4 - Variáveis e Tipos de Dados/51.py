x, y = map(float, input('Informe um x seguido de um y em coordeanas cartesianas: ').split())
print(f'A distância de ({x}, {y}) e (0, 0) é {(x**2 + y**2)**0.5:.2f}')