s = 0
contador = 0
for c in range(1, 501):
    if c % 3 == 0:
        if c % 2 != 0:
            s = s + c
            contador = contador + 1
print('São {} números, somando o total de {}.'.format(contador, s))
