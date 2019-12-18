venda_mensal = float(input('Informe o valor da venda: R$ '))
comissao = 'Erro de cálculo' #caso por algum motivo do além ele não passe em nenhum if, irá imprimir isso
if venda_mensal < 10_000:
    comissao = 'Demitido'
elif venda_mensal < 20_000:
    comissao = 400 + 1.14*venda_mensal
elif venda_mensal < 40_000:
    comissao = 500 + 1.14*venda_mensal
elif venda_mensal < 60_000:
    comissao = 550 + 1.14*venda_mensal
elif venda_mensal < 80_000:
    comissao = 600 + 1.14*venda_mensal
elif venda_mensal < 100_000:
    comissao = 650 + 1.14*venda_mensal
elif venda_mensal >= 100_000:
    comissao = 700 + 1.16*venda_mensal
if type(comissao) == str:
    print(comissao)
else:
    print(f'Comissão: R$ {comissao:.2f}')
