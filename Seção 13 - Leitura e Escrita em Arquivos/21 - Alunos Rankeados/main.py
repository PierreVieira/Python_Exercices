from pickle import dump, load


def pegar_info_entrada():
    """
    Primeiro contato do programa com o usuário.
    :return: Lista de alunos e o número de alunos.
    """
    numero_alunos = int(input('Informe a quantidade de alunos que deseja cadastrar: '))
    lista_alunos = []
    for c in range(numero_alunos):
        nome = input(f'Informe o nome do {c + 1}º aluno: ').title()
        nota = float(input(f'Informe a nota de {nome}: '))
        lista_alunos.append({'nome': nome, 'nota': nota})
    return lista_alunos, numero_alunos


def registrar_entrada_no_arquivo(lista_alunos):
    """
    Pega a entrada e registra em um arquivo binário.
    :param lista_alunos: lista que contém vários dicionários de alunos com nome e nota.
    :return: None.
    """
    with open('alunos.dat', 'wb') as arq:
        for aluno in lista_alunos:
            dump(aluno, arq)


def pegar_entrada_arquivo(numero_alunos):
    """
    Pega as informações do arquivo binário e registra em uma lista.
    :param numero_alunos: número de alunos da lista.
    :return: Os alunos presentes no arquivo.
    """
    alunos_arquivo = []
    with open('alunos.dat', 'rb') as arq:
        for c in range(numero_alunos):
            alunos_arquivo.append(load(arq))
    return alunos_arquivo


def maior_nota_de_todas():
    """
    Printa personalizado (colorido) a maior nota.
    :return: None.
    """
    print('\n\033[0;30mA maior nota foi\033[m', end=' ')
    print(f'\033[0;32m{maior_nota}\033[m')


def melhores_alunos_de_todos():
    """
    Printa personalizado (colorido) os melhores alunos.
    :return: None.
    """
    mensagem = '========= MELHORES ALUNOS ========='
    print(f'\n\033[1;31m{mensagem}\033[m')
    for nome_aluno in melhores_alunos:
        print(f"\033[0;34m{nome_aluno.center(len(mensagem))}\033[m")
    print(f'\033[1;31m{"=" * len(mensagem)}\033[m')


def alunos_rankeados():
    """
    Printa personalizado (colorido) o ranking dos alunos (do melhor ao pior).
    :return: None.
    """
    mensagem = '========= RANKING DE ALUNOS ========='
    print(f'\n\033[1;31m{mensagem}\033[m')
    c = 1
    ranking_alunos.reverse()
    ultima_nota = ranking_alunos[0]['nota']
    for aluno in ranking_alunos:
        if ultima_nota != aluno['nota']:
            ultima_nota = aluno['nota']
            c += 1
        print(f"\033[0;32m{c}º: {aluno['nome']}\033[m", end=' ')
        print(f"\033[0;36m{int(aluno['nota'])}\033[m")
    print(f'\033[1;31m{"=" * len(mensagem)}\033[m')


def informacoes():
    """
    Exibe as informações principais obtidas da execução do programa (maior nota, melhores alunos e ranking).
    :return: None.
    """
    maior_nota_de_todas()
    melhores_alunos_de_todos()
    alunos_rankeados()


def rankear_alunos():
    """
    Faz rankeamento dos alunos.
    :return: None.
    """
    rankeados = []
    for nota in sorted(notas):
        for aluno in alunos_arquivo:
            if aluno['nota'] == nota:
                rankeados.append(aluno)
                alunos_arquivo.remove(aluno)
    return rankeados


infos_entrada = pegar_info_entrada()
registrar_entrada_no_arquivo(infos_entrada[0])
alunos_arquivo = pegar_entrada_arquivo(infos_entrada[1])
notas = [aluno.get('nota') for aluno in alunos_arquivo]
maior_nota = max(notas)
melhores_alunos = [aluno.get('nome') for aluno in alunos_arquivo if aluno['nota'] == maior_nota]
ranking_alunos = rankear_alunos()
informacoes()
