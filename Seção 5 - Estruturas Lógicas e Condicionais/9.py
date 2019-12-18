salario = float(input('Informe o salário em reais: '))
valor_prestacao = float(input('Informe o valor da prestação do empréstimo: '))
if valor_prestacao > salario*0.2:
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')
