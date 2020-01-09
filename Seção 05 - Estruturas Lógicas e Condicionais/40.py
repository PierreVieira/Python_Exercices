custo_de_fabrica = float(input('Informe o custo de fábrica: R$ '))
if custo_de_fabrica <= 12_000:
    custo_consumidor = 0.05*custo_de_fabrica
elif custo_de_fabrica <= 25_000:
    custo_consumidor = 0.25*custo_de_fabrica
else:
    custo_consumidor = 0.35*custo_de_fabrica
print(f'Custo do consumidor: R$ {custo_de_fabrica + custo_consumidor:.2f}')
