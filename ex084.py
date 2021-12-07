#Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
nome = list()
geral = list()

maisp = menosp = ''

while True:
    nome.append(str(input('Nome: ')))
    nome.append(float(input(('Peso (kg): '))))
    geral.append(nome[:])
    nome.clear()
    resp = input('Deseja continuar?(s/n)')
    if resp in 'Nn':
        break

for c in range(len(geral)):
    if c == 0:
        menosp = geral[c][0]
    if geral[c][0] > maisp:
        maisp = geral[c][0]
    else:
        menosp = geral[c][0]

print(f'foram cadastrados {len(geral)} pessoas')
print(f'O menor pesso foi: {menosp}')
print(f'O maior peso foi : {maisp}')

