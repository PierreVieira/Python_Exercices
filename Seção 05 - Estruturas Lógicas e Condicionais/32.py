print('[100] Cachorro quente: R$ 1.20')
print('[101] Bauru simples: R$ 1.30')
print('[102] Cachorro com ovo: R$ 1.50')
print('[103] Hamburguer: R$ 1.20')
print('[104] Cheeseburguer: R$ 1.70')
print('[105] Suco: R$ 2.20')
print('[106] Refrigerante: R$ 1.00')
opcao = int(input('Escolha uma opção informando o código: '))
if not(100 <= opcao <= 106):
    print('Opção não válida!')
else:
    qtde = int(input('Informe quantas unidades do ítem {} você deseja levar: '.format(opcao)))
    print('Preço total a pagar: R$ ', end='')
    if opcao == 100:
        print(f'{qtde*1.2:.2f}')
    elif opcao == 101:
        print(f'{qtde * 1.3:.2f}')
    elif opcao == 102:
        print(f'{qtde * 1.5:.2f}')
    elif opcao == 103:
        print(f'{qtde * 1.2:.2f}')
    elif opcao == 104:
        print(f'{qtde * 1.7:.2f}')
    elif opcao == 105:
        print(f'{qtde * 2.2:.2f}')
    else:
        print(f'{qtde:.2f}')
