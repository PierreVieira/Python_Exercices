def preenche_arquivo(arquivo):
    while True:
        caractere = input('Informe um caractere: ')
        if caractere == '0':
            break
        else:
            arquivo.write(caractere)


def le_arquivo(arquivo):
    arquivo.seek(0)
    print(arquivo.read())


with open('arq.txt', 'w+') as arquivo:
    preenche_arquivo(arquivo)
    le_arquivo(arquivo)
