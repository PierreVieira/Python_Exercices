numero = int(input('Informe um número para ver se é divísivel por 3 ou 5 mas não por ambos: '))
if numero % 3 == 0 and numero % 5 == 0:
    print(f'O número {numero} é divisível por 3 e 5')
elif numero % 3 == 0:
    print(f'O número {numero} é divisível por 3')
elif numero % 5 == 0:
    print(f'O número {numero} é divisível por 5')
else:
    print(f'O número {numero} não é divisível nem por 3 e nem por 5')
