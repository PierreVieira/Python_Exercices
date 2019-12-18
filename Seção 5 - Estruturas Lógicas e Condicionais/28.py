print('[0] Geométrica\n[1] Ponderada\n[2] Harmônica\n[3] Aritmética')
opcao = int(input('Escolha uma média: '))
if not(0 <= opcao <= 3):
    print('Opção inválida! Tente novamente.')
else:
    x, y, z = map(int, input('Informe três números: ').split())
    if opcao == 0: #Geométrica
        media = (x*y*z)**(1/3)
    elif opcao == 1: #Ponderada
        media = (x + 2*y + 3*z)/6
    elif opcao == 2: #Harmônica
        if x == 0 or y == 0 or z == 0:
            media = 'Tende a zero' #Denominador tende para o infinito.
        else:
            media = 1/(1/x + 1/y + 1/z)
    else: #Aritmética
        media = (x + y + z)/3
    if type(media) == str:
        print(media)
    else:
        print(f'Média: {media:.3f}')
