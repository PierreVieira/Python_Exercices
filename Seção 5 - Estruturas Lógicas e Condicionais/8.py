a, b = map(float, input('Informe duas notas: ').split())
if not(0 <= a <= 10):
    print('Primeira nota não é válida! Digite um valor que esteja dentro do intervalo [0, 10]')
elif not(0 <= b <= 10):
    print('Segunda nota nãe é válida! Digite um valor que esteja dentro do intervalo [0, 10]')
else:
    print(f'Média das notas: {(a+b)/2}')
