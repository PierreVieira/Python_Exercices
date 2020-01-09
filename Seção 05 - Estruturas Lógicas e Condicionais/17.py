base_maior, base_menor, altura = map(float, input('Informe em sequênica: a base maior, menor e altura do trapézio: ').split())
if base_maior <= 0 or base_menor <= 0 or altura <= 0:
    print('Existe(m) valor(es) que não atende(m) às condições!\nPor favor informe apenas valores maiores que 0.')
else:
    if base_menor > base_maior: #Se a base menor for maior que a base maior
        base_menor, base_maior = base_maior, base_menor #Troque as bases
    area = (base_maior + base_menor)*altura/2
    print(f'Base maior: {base_maior}\nBase menor: {base_menor}\nAltura: {altura}\nÁrea: {area:.3f}')
