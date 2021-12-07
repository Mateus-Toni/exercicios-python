def metade(valor):
    return moeda(valor / 2)


def dobro(valor):
    return moeda(valor * 2)


def aumentar(valor, taxa):
    return moeda(valor * (100 + taxa) / 100)


def diminuir(valor, taxa):
    return moeda(valor * (100 - taxa) / 100)


def moeda(numero):
    texto = str(round(numero, 2))
    resp = ""
    contador = 0
    virgula = False
    for char in texto:
        if char == '.':
            resp += ','
            virgula = True
            continue
        else:
            resp += char
        if virgula == True:
            contador += 1
    if contador == 0:
        resp += ',00'
    elif contador == 1:
        resp += '0'
    return resp

Depois deixei igual sua resolução (para simplificar). Por último, minha função principal ficou:

from modulos import moeda2

print('=' * 12 + 'Desafio 108' + '=' * 12)
moeda = input('Digite a moeda: ')
numero = float(input(f'Digite o valor em {moeda}: '))
numero = round(numero, 2)
print(f'O dobro de {moeda} {moeda2.moeda(numero)} é {moeda} {moeda2.dobro(numero)}.')
print(f'A metade de {moeda} {moeda2.moeda(numero)} é {moeda} {moeda2.metade(numero)}.')
print(f'Aumentando 10% de {moeda} {moeda2.moeda(numero)}, temos {moeda} {moeda2.aumentar(numero, 10)}.')
print(f'Diminuindo 10% de {moeda} {moeda2.moeda(numero)}, temos {moeda} {moeda2.diminuir(numero, 10)}.')