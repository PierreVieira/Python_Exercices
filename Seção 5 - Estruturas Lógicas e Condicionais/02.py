numero = float(input('Digite um número: '))
if numero < 0:
    print('Número inválido para o cálculo de raíz quadarada')
else:
    print('Raíz quadrada de {} = {:.3f}'.format(numero, numero**0.5))
