tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    numero = int(input('Digite um número entre 0 e 10: '))
    if 0 <= numero <= 10:
        print(f'{numero} escrito ficaria : {tupla[numero]}')
        break
    else:
        print('tente de novo')


