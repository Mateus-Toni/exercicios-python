from random import randint

jogo = list()
jogos = list()
n = 0

print('='*32)
print('          MEGA SENNA')
print('='*32)

n = int(input('Quantos jogos você comprou? : '))
print('='*32)

#Nesse bloco vão ser gerados os números para cada jogo:
for c in range(n):
    while True:
        v = randint(1,60)
        if v not in jogo:
            jogo.append(v)
        if 6 == len(jogo):
            break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()

#Nesse bloco serão mostrados os possíveis jogos:
print('='*32)
for x in range(n):
    print('Jogo {}: {}'.format(x+1,jogos[x]))
print('='*32)
print('='*9,'Boa Sorte =)','='*9)