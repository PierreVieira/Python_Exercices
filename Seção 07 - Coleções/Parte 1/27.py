v = [] #Armazenará a entrada do usuário
for c in range(10):
    v.append(int(input(f'Informe o {c+1}° valor: ')))
v1 = [] #Armazenará os ímpares
v2 = [] #Armazenará os pares
for elemento in v:
    if elemento%2 == 1: #Se o elemento for ímpar...
        v1.append(elemento) #Armazena no 'vetor' (lista) dos ímpares
    else: #Sendo o elemento par
        v2.append(elemento) #Armazena no 'vetor' (lista) dos pares
print(f'Pares: {v2}\nÍmpares: {v1}')
