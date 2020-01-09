peso = float(input('Informe o seu peso em quilogramas: '))
altura = float(input('Informe a sua altura em metros: '))
imc = peso/(altura**2)
print(f'IMC: {imc:.2f}')
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 24.9:
    print('Saudável')
elif imc < 29.9:
    print('Peso em excesso')
elif imc < 34.9:
    print('Obesidade Grau I')
elif imc < 39.9:
    print('Obesidade Grau II (severa)')
else:
    print('Obesidade Grau III (mórbida)')
