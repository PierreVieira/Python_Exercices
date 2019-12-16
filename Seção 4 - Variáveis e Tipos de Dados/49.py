hora, minuto, segundo = map(int, input('Informe hora, minuto e segundo do início da operação: ').split())
duracao = int(input('Informe a duração em segundos: '))
acrescimo_hora = duracao//3600
acrescimo_minuto = (duracao - acrescimo_hora*3600)//60
acrescimo_segundo = duracao - (acrescimo_hora*3600 + acrescimo_minuto*60)
hora += acrescimo_hora
minuto += acrescimo_minuto
segundo += acrescimo_segundo
print(f'Término: {hora:2}:{minuto:2}:{segundo:2}')
