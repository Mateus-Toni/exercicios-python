valor1 = float(input('Digite o 1 valor: '))
valor2 = float(input('Digite o 2 valor: '))
finalizar = False
while not finalizar:
    menu = int(input('''Agora, insira o número que corresponde ao que você quer fazer com seus valores
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA:    '''))
    soma = valor1 + valor2
    mult = valor1 * valor2
    maiorvalor = ''
    if menu == 1:
        print('A soma dos valores é de {}.'.format(soma))
    if menu == 2:
        print('A multiplicação entre os valores é de {}.'.format(mult))
    if menu == 3:
        if valor1 > valor2:
            maiorvalor = valor1
            print('O maior valor entre os dois inseridos é de {}.'.format(maiorvalor))
        if valor2 > valor1:
            maiorvalor = valor2
            print('O maior valor entre os dois inseridos é de {}.'.format(maiorvalor))
        if valor2 == valor1:
            print('Os dois valores são iguais!')
    if menu == 4:
        print('Seu desejo é uma ordem!')
        valor1 = int(input('Insira o novo 1 valor: '))
        valor2 = int(input('Insira o novo 2 valor: '))
    if menu == 5:
        print('Entendido, estamos finalizando o programa! Tchauzinho! :)')
        finalizar = True
    print('-='*10)
