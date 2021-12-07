def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    print('\n', '-' * 30, sep='')
    f = 1
    for cont in range(n, 0, -1):
        if show:
            print(cont, end=' x ' if cont > 1 else ' = ')
        f *= cont
    return f


# Programa Principal
while True:
    print('''
        [ 0 ] Apenas o fatorial;
        [ 1 ] Fatorial com conta;
        [ 2 ] Ajuda interativa do comando;
        [ 3 ] Sair.
        ''')

    while True:
        opt = int(input('Opção: '))
        if opt in range(4):
            break
        print('ERRO. Opção inválida, tente novamente.')

    if opt in [0, 1]:
        num = int(input('\nNúmero a ser calculado: '))
        print(fatorial(num, bool(opt)))
    elif opt == 2:
        help(fatorial)
    else:
        break