a, b, c = map(float, input('Informe os três lados do triângulo: ').split())
if not(a < b + c and b < a + c and c < a + b):
    print('Os lados informados não formam um triângulo!')
else:
    if a == b == c:
        print('TRIÂNGULO EQUILÁTERO')
    elif a == b or b == c or a == c:
        print('TRIÂNGULO ISÓCELES')
    else:
        print('TRIÃNGULO ESCALENO')
