Módulo:
def metade(n, show=False):
    n = n / 2
    if show:
        return moeda(n)
    else:
        return n


def dobro(n, show=False):
    n = n * 2
    if show:
        return moeda(n)
    else:
        return n


def aumentar(n, per, show=False):
    n = n + ((n * per) / 100)
    if show:
        return moeda(n)
    else:
        return n


def diminuir(n, per, show=False):
    n = n - ((n * per / 100))
    if show:
        return moeda(n)
    else:
        return n


def moeda(n):
    return f'R${n:.2f}'


def resumo(n, a, d):
    print('=' * 60)
    print(f'{"RESUMO DE VALORES":-^60}')
    print('=' * 60)
    print(f'Preço analizado:R${n:.2f}')
    print(f'Dobro do preço: {dobro(n, True)}')
    print(f'Metade do preço:{metade(n, True)}')
    print(f'{a}% de aumento:{aumentar(n, a, True)}')
    print(f'{d}% de redução:{diminuir(n, d, True)}')
    print('-' * 60)


Programa:
from uteis import moeda

p = (float(input('Informe um preço: R$')))
print(f'A metade do preço é {moeda.metade(p)}')
print(f'O dobro do preço é {moeda.dobro(p)}')
print(f'Aumentando 10% fica {moeda.aumentar(p, 10)}')
print(f'Diminuindo 13% fica {moeda.diminuir(p, 13)}'