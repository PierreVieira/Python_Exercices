segundos = int(input('Informe um valor inteiro em segundos: '))
horas = segundos//3600
minutos = (segundos - (horas*3600))//60
segundos = segundos - (horas*3600 + minutos*60)
print(f'{horas:2}:{minutos:2}:{segundos:2}')