#Inicialização das variáveis
matriz = []
linha_maior = 0
coluna_maior = 0
#Esse for vai gerar a matriz de fato
for c in range(4):
    lista_entrada_usuario = input('Informe os 4 elementos da primeira linha separando-os por espaço: ').split() #Cria uma lista com 4 elementos
    matriz.append(list(map(int, lista_entrada_usuario))) #Aqui estou criando uma lista com os valores informados pelo usuário mapeados para o tipo int
    #Em python uma matriz é uma lista de listas
#Esse for vai printar a matriz
for linha in matriz: #Pega linha por linha da matriz (lista por lista)
    for elemento in linha: #Pega elemento por elemento da linha
        print(f'[{elemento}]', end=' ')
    print() #Print vazio para saltar a linha
maior = matriz[0][0] #Digo que o maior elemento está na posição [0][0]
#Esse for vai identificar qual o maior elemento da matriz, identificando, tembém sua linha e coluna
for c in range(len(matriz)):
    for d in range(len(matriz)):
        if matriz[c][d] > maior:
            maior = matriz[c][d]
            linha_maior = c
            coluna_maior = d
print(f'O maior elemento é {maior}\nLinha: {linha_maior}\nColuna: {coluna_maior}')
