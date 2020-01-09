from math import log
numero = int(input('Digite um número inteiro: '))
if numero < 0:
    print('Número inválido')
else:
    print(f'Log de {numero} = {log(numero):.3f}')
