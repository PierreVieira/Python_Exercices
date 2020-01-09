def inverter(n):
    s = ''
    for c in range(len(n)-1, -1, -1):
        s += n[c]
    return s

while True:
    numero = input('Informe um número de 3 dígitos: ')
    if len(numero) == 3:
        break
print('{} invertido = {}'.format(numero, inverter(numero)))
