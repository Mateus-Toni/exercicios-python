num = int(input('Digite um número qualquer: '))
d = 0
for c in range(1, num + 1):
    if num % c == 0:
        d += 1
if d == 2:
    print('Esse número é primo')
else:
    print('Esse número nao é primo')
