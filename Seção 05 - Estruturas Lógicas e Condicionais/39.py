salario_atual = float(input('Informe o seu salário: R$ '))
tempo_de_servico = float(input('Informe o seu tempo de serviço em anos: '))
if salario_atual < 500:
    reajuste = 0.25
elif salario_atual < 1000:
    reajuste = 0.20
elif salario_atual < 1500:
    reajuste = 0.15
elif salario_atual < 2000:
    reajuste = 0.10
else:
    reajuste = 0
if tempo_de_servico < 1:
    bonus = 0
elif tempo_de_servico < 3:
    bonus = 100
elif tempo_de_servico < 6:
    bonus = 200
elif tempo_de_servico < 10:
    bonus = 300
else:
    bonus = 500
print(f'Salário reajustado: R$ {salario_atual*(1+reajuste) + bonus:.2f}')
