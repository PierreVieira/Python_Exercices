from math import factorial, radians


def seno(angulo_radianos):
    max_iteracoes = 70
    somatorio = 0.0
    for n in range(max_iteracoes):
        somatorio += ((-1)**n)*(angulo_radianos**(2*n+1))/(factorial(2*n+1))
    return somatorio


angulo = float(input('Informe um angulo em graus: '))
print(f'O seno de {angulo}° é {seno(radians(angulo)):.3f}')
