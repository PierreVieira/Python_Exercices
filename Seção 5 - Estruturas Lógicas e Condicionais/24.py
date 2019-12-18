preco = float(input('Preço da mercadoria: R$ '))
estado = input('Informe o estado [MG/SP/RJ/MS]: ').upper()
if estado != 'MG' and estado != 'SP' and estado != 'RJ' and estado != 'MS':
    print('Estado informado não é válido')
else:
    if estado == 'MG':
        preco *= 1.07
    elif estado == 'SP':
        preco *= 1.12
    elif estado == 'RJ':
        preco *= 1.15
    else:
        preco *= 1.08
    print(f'Preço final: R$ {preco:.2f}')
