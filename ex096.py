def area(l, c):
    ar = l * c
    print(f'A área de um terreno {l}x{c} é de {ar}m²')


print('Controle de Trrenos')
print('-'*20)
area(l=float(input('LARGURA (m): ')), c=float(input('COMPRIMENTO (m): ')))