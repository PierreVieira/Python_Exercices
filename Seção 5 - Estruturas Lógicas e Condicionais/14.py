n1, n2, n3 = map(float, input('Informe as notas trabalho de laboratório, avaliação semestreal e exame final respectivamente: ').split())
if n1 > 10 or n2 > 10 or n3 > 10 or n1 < 0 or n2 < 0 or n3 < 0:
    print('Nota(s) inválida(s)! Digite apenas notas que estejam no intervalo [0, 10]')
else:
    media = (n1*2 + n2*3 + n3*5)/10
    if media <= 2.9:
        print('REPROVADO')
    elif media <= 4.9:
        print('RECUPERAÇÃO')
    else:
        print('APROVADO')
    print(f'Média: {media:.2f}')
