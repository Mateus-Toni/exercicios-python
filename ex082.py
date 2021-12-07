num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('a')))
    r = input('resp')
    if r in 'Nn':
        break

for c in range(len(num)):
    if num[c] % 2 == 0:
        pares.append(num[c])
    else:
        impares.append((num[c]))

print(num)
print(pares)
print(impares)
