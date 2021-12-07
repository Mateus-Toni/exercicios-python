d = dict()
l = list()
c = list()
tot = j = h = 0
while True:
    d.clear()
    c.clear()
    d['nome'] = str(input('Nome do Jogador: '))
    d['jogos'] = int(input(f'Quantos jogos {d["nome"]} jogou? '))
    j+=1
    for x in range (1,d['jogos']+1):
        gols = int(input(f'Quantos gols marcou na partida {x}? '))
        c.append(gols)
        tot = sum(c)
        d['gols'] = c[:]
        d['total'] = tot
    l.append(d.copy())
    while True:
        q = str(input('Deseja continuar [S/N]? ')).upper()[0]
        if q in "SN":
            break
        print('Erro! Digite apenas S ou N!')
    if q == 'N':
        break
    print('-'*30)
print('*'*80)
print(f'{str("cod"):>3}', end=' //')
for i in d.keys():
    print(f'{i:^16}', end='//')
print()
print('-'*80, end='')
for dados in l:
    print()
    print(f'{h:^3}', end='//')
    h+=1
    for k,v in dados.items():
        print(f"{str(v):^16}",end='//')
    print()
while True:
    u = int(input('Mostrar os dados de qual jogador (digite o código correspondente ou 999 para parar)? '))
    if u == 999:
        print("Obrigado!")
        break
    if u > j:
        print(f'Erro! Não existe jogador com o código {u}!')
    else:
        print(f'---> Levantamento do jogador de {l[u]["nome"].upper()}: ')
        for k,v in enumerate(l[u]["gols"]):
            print(f'No jogo {k+1} fez {v} gol(s)!')