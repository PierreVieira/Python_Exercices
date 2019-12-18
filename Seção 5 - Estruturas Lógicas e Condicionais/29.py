from random import randint
cont = 0
for c in range(5):
    a = randint(1, 100)
    b = randint(1, 100)
    resposta = int(input(f'{a} + {b} = '))
    if resposta == a + b:
        cont += 1
if cont == 1:
    print('Você acertou 1 questão!')
else:
    print(f'Você acertou {cont} questões')
