from datetime import datetime
idade = int(input('Informe a sua idade: '))
ano_atual = datetime.now().year
nascimento = ano_atual - idade
print('Você nasceu em {}'.format(nascimento))
