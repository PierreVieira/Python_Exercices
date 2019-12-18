lista = []
n = 1
while n <= 100:
    lista.append(n)
    n+=1
print(lista)
lista.clear()
for c in range(1, 101):
    lista.append(c)
print(lista)
lista.clear()
n = 1
while True:
    if n == 101:
        break
    lista.append(n)
    n+=1
print(lista)
