valor_hora = float(input('Informe o valor da hora trabalhada: '))
numero_horas = float(input('Informe quantas horas foram trablhadas: '))
pago = valor_hora*numero_horas*1.1
print('Deve ser pago R$ {:.2f} ao funcionário'.format(pago))
