def sort(valor):
    lista = []
    for c in range(0, valor):
        lista.append(randint(0, 10))
    print(f'Sorteando {valor} valores da lista: ', end='')
    for c in lista:
        print(f'{c}', end=' ')
        sleep(0.3)
    print('PRONTO!')
    def pares(par):
        soma = 0
        for c in par:
            if c % 2 == 0:
                soma += c
        print(f'Somando os valores pares de {lista}, temos {soma}')
    pares(lista)


sort(5)