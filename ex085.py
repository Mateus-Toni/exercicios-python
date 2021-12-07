pares = list()
impares =list()
geral = list()
for c in range(7):
    v = int(input('Digite um número: '))
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

pares.sort()
impares.sort()
geral.append(pares[:])
geral.append(impares[:])
print(geral)



