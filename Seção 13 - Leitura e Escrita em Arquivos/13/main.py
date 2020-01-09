with open('arq.txt', 'a') as arq:
    while True:
        nome = input('Informe o nome da pessoa: ').title()
        telefone = input(f'Informe o telefone de {nome}: ')
        if telefone == '0':
            break
        string = nome + ';' + telefone + '\n'
        arq.write(string)

