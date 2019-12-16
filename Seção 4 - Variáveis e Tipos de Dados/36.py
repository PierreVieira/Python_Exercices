from math import pi
altura, raio = map(float, input('Informe a altura e em seguida o raio do cilindro: ').split())
print('Volume: {:.2f}'.format(pi*raio**2*altura))
