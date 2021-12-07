lista = list()
for c in range(1, 6):
    lista.append(int(input('Qual o peso da {}ª pessoa? ' .format(c))))
print('O maior peso é', max(lista))
print('O menor peso é', min(lista))
