def contador(a=1, b=1, intervalo=1, personalizar='n'):
    from time import sleep
    print(f'{20 * "-="}')
    if personalizar != 's':
        print(f'contagem de {a} até {b} de {intervalo} em {intervalo}')
        lst_r = list(range(a, b + 1, intervalo))
        if a < b:
            for n in range(a, b + 1, intervalo):
                if n == max(lst_r):
                    print(f'{n} FIM')
                else:
                    print(f'{n} ', end='')
                    sleep(0.5)
        elif a > b:
            lst_r = list(range(a, b - 1, intervalo))
            for n in range(a, b - 1, intervalo):
                if n == min(lst_r):
                    print(f'{n} FIM')
                else:
                    print(f'{n} ', end='')
                    sleep(0.5)
    else:
        print('Agora é sua vez de personalizar a contagem!')
        a = int(input('inicio: '))
        b = int(input('fim: '))
        intervalo = int(input('passo: '))
        print(f'{20 * "-="}')
        print(f'contagem de {a} até {b} de {intervalo} em {intervalo}')
        lst_r = list(range(a, b + 1, intervalo))
        if a < b:
            for n in range(a, b + 1, intervalo):
                if n == max(lst_r):
                    print(f'{n} FIM')
                else:
                    print(f'{n} ', end='')
                    sleep(0.5)
        elif a > b:
            lst_r = list(range(a, b - 1, intervalo))
            for n in range(a, b - 1, intervalo):
                if n == min(lst_r):
                    print(f'{n} FIM')
                else:
                    print(f'{n} ', end='')
                    sleep(0.5)


# programa principal
contador(1, 10, 1)
contador(10, 0, -2)
contador(personalizar='s')