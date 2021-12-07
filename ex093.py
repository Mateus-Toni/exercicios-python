jogador = {
    'nome': str(input('Nome do jogador: ')),
    'partidas': int(input('Total de partidas: '))
}
gol_p = []
for i in range(0,jogador['partidas']):
    gol_p.append(int(input(f'Nº de gols na {i+1}o partida: ')))
jogador['gols'] = gol_p
jogador['total'] = sum(gol_p)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'A chave {k} apresenta o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i in range(0,jogador['partidas']):
    print(f'    => Na {i+1}o partida, {jogador["nome"]} fez {jogador["gols"][i]} gol(s)')
print(f'No total, foram {jogador["total"]} gols.')