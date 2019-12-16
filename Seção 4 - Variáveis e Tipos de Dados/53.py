comprimento, largura = map(float, input('Informe o comprimento e em seguido a largura do terreno: ').split())
preco = float(input('Informe o preço por metro de tela: '))
custo = preco*(2*comprimento + 2*largura)
print(f'O custo é de R$ {custo:.2f}')
