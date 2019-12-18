a, b, c = map(float, input('Digite três notas: ').split())
media = (a + b + 2*c)/4
if media >= 60:
    print('APROVADO')
else:
    print('REPROVADO')
print(f'Média: {media:.2f}')
