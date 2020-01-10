numero_alunos = int(input('Informe a quantidade de alunos que deseja cadastrar: '))
lista_alunos = []
for c in range(numero_alunos):
    nome = input(f'Informe o nome do {c + 1}º aluno: ').title()
    nota = float(input(f'Informe a nota de {nome}: '))
    lista_alunos.append({'nome': nome, 'nota': nota})
print(lista_alunos)
with open('alunos.txt', 'w') as arq:
    for aluno in lista_alunos:
        arq.write(aluno.get('nome')+';'+str(aluno.get('nota')))
        arq.write('\n')