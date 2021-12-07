dados = dict()
gols = list()
somagols = 0
dados['nome'] = str(input('Digite o nome do jogador: '))
c = int(input('Quantos jogos ele jogou? : '))
for d in range(c):
    gols.append(int(input(f'Quantos gols no {d+1}o jogo: ')))
dados['gols'] = gols[:]
for f in range(len(gols)):
    somagols = somagols + gols[f]

dados['totaldegols'] = somagols
print(dados)

print('Jogador {} jogou {} jogos e fez:'.format(dados['nome'],c))
for d,x in enumerate(gols):
    print('no {}o jogo ele fez {} gols'.format(d+1,x))

print(dados['totaldegols'])

