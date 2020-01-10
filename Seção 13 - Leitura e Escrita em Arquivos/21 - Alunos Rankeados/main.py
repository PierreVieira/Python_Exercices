from pickle import dump, load
def pegar_entrada_arquivo():
    numero_alunos = int(input('Informe a quantidade de alunos que deseja cadastrar: '))
    lista_alunos = []
    alunos_arquivo = []
    for c in range(numero_alunos):
        nome = input(f'Informe o nome do {c + 1}º aluno: ').title()
        nota = float(input(f'Informe a nota de {nome}: '))
        lista_alunos.append({'nome': nome, 'nota': nota})
    with open('alunos.dat', 'wb') as arq:
        for aluno in lista_alunos:
            dump(aluno, arq)
    with open('alunos.dat', 'rb') as arq:
        for c in range(numero_alunos):
            alunos_arquivo.append(load(arq))
    return alunos_arquivo


def maior_nota_de_todas():
    print('\n\033[0;30mA maior nota foi\033[m', end=' ')
    print(f'\033[0;32m{maior_nota}\033[m')


def melhores_alunos_de_todos():
    mensagem = '========= MELHORES ALUNOS ========='
    print(f'\n\033[1;31m{mensagem}\033[m')
    for nome_aluno in melhores_alunos:
        print(f"\033[0;34m{nome_aluno.center(len(mensagem))}\033[m")
    print(f'\033[1;31m{"=" * len(mensagem)}\033[m')


def alunos_rankeados():
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
    maior_nota_de_todas()
    melhores_alunos_de_todos()
    alunos_rankeados()


def rankear_alunos():
    rankeados = []
    for nota in sorted(notas):
        for aluno in alunos_arquivo:
            if aluno['nota'] == nota:
                rankeados.append(aluno)
                alunos_arquivo.remove(aluno)
    return rankeados


alunos_arquivo = pegar_entrada_arquivo()
notas = [aluno.get('nota') for aluno in alunos_arquivo]
maior_nota = max(notas)
melhores_alunos = [aluno.get('nome') for aluno in alunos_arquivo if aluno['nota'] == maior_nota]
ranking_alunos = rankear_alunos()
informacoes()
