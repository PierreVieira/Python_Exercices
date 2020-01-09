preco = float(input('Informe o preço da mercadoria: '))
if preco <= 50:
    preco *= 1.05
elif preco <= 100:
    preco *= 1.1
else:
    preco *= 1.15
print(f'Novo preço: R$ {preco:.2f}')
if preco <= 80:
    print('Barato')
elif preco <= 120:
    print('Normal')
elif preco <= 200:
    print('Caro')
else:
    print('Muito caro')
