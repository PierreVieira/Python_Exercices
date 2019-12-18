distancia = float(input('Informe a distância percorrida em quilômetros: '))
litros = float(input('Informe a quantidade de litros gastos: '))
quilometros_por_litro = distancia/litros
if quilometros_por_litro < 8:
    print('Venda o carro!')
elif quilometros_por_litro <= 14:
    print('Econômico!')
else:
    print('Super econômico!')
