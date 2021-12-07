from time import sleep
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 0
tot = 0
while cont != 10:
    print(p, end=', ')
    cont += 1
    p += r
    tot += 1
    if cont == 10:
        print('PAUSA')
        sleep(1)
        pa = str(input('\nDeseja continuar? [S/N]'))
        if pa in 'Ss':
            t = int(input('Quantos termos você quer mostrar a mais? '))
            cont -= t
print('=' * 30)
print('Progressão finalizada. Foram mostrados {} termos.'.format(tot))
