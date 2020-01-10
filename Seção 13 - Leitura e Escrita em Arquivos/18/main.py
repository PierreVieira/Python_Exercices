with open('compras.txt') as arq:
    preco = 0
    for produto in arq.readlines():
        preco += float(produto[produto.find(';')+1::])
print(f'O preço total a se pagar é R$ {preco:.2f}')
