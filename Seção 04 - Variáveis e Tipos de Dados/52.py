jogador1, jogador2, jogador3 = map(float, input('Informe os 3 valores de aposta: ').split())
premio = float(input('Informe o valor do prêmio: '))
soma = jogador3+jogador2+jogador1
v1 = premio*(jogador1/soma)
v2 = premio*(jogador2/soma)
v3 = premio*(jogador3/soma)
print(f'Jogador 1: R$ {v1:.2f}\nJogador 2: R$ {v2:.2f}\nJogador 3: R$ {v3:.2f}')
