numero = int(input('Digite um número inteiro entre 1 e 7: '))
if numero == 1:
    print('DOMINGO')
elif numero == 2:
    print('SEGUNDA')
elif numero == 3:
    print('TERÇA')
elif numero == 4:
    print('QUARTA')
elif numero == 5:
    print('QUINTA')
elif numero == 6:
    print('SEXTA')
elif numero == 7:
    print('SÁBADO')
else:
    print('Não existe dia da semana para o número informado!\nPor favor informe um valor que esteja no intervalo [1, 7].')
