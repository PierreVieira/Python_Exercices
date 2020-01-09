idade_nadador = int(input('Informe a idade do(a) nadodor(a): '))
if idade_nadador < 5:
    print('Muito novo(a) para ser um nadador(a)')
elif idade_nadador <= 7:
    print('Infantil A')
elif idade_nadador <= 10:
    print('Infantil B')
elif idade_nadador <= 13:
    print('Juvenil A')
elif idade_nadador <= 17:
    print('Juvenil B')
else:
    print('Sênior')
