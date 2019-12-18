a, b = map(int, input('Digite dois números inteiros: ').split())
if a > b:
    print(f'Maior: {a}')
else:
    print(f'Maior: {b}')
print(f'Diferença entre os números informados: {abs(a - b)}')
