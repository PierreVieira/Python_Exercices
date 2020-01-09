a, b = map(float, input('Informe dois valores A e B: ').split())
print('=========== Esoclha uma operação ===========')
operacao = int(input('[0] SOMA\n[1] SUBTRAÇÃO\n[2] MULTIPLICAÇÃ0\n[3] DIVISÃO\nOperação: '))
if b == 0 and operacao == 3:
    print('Não existe divisão por 0')
elif not(0 <= operacao <= 3):
    print('Você digitou um valor inválido para a operação!\nDigite apenas um valor que esteja no invervalo [0, 3]')
else:
    if operacao == 0: #soma
        print(f'{a} + {b} = {a + b}')
    elif operacao == 1: #subtração
        if a >= b:
            print(f'{a} - {b} = ', end='')
        else:
            print(f'{b} - {a} = ', end='')
        print(f'{abs(a - b)}')
    elif operacao == 2: #multiplicação
        print(f'{a} * {b} = {a * b}')
    else: #divisão
        print(f'{a} / {b} = {a / b}')
