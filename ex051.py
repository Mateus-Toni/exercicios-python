pt = int(input('1° termo: '))
r = int(input('Razão: '))
for c in range(pt, pt + 10 * r, r):
    print(c, end=' ')
