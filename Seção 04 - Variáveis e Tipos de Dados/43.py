valor_total = float(input('Informe um valor em reais: '))
total_com_desconto = 0.9*valor_total
valor_de_cada_parcela = valor_total/3
comissao_vendedor1 = total_com_desconto*0.05
comissao_vendedor2 = valor_total*0.05
print(f'Valor total: R$ {valor_total:.2f}\nTotal com desconto: R$ {total_com_desconto:.2f}')
print(f'Valor de cada parcela: R$ {valor_de_cada_parcela:.2f}')
print('Valor da comissão do vendedor na compra à vista: R$ {:.2f}'.format(comissao_vendedor1))
print('Valor da comissão do vendedor na compra à prazo: R$ {:.2f}'.format(comissao_vendedor2))
