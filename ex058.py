from random import randint
from time import sleep

c = 's'
contador = 0
contadorpc = 0
jogador = 0
print('-+=-' * 20)
nome = str(input('Qual seu nome jogador ? ')).strip()
print('-*-' * 20)
nivel = int(input(f'''Em qual nivel você deseja jogar {nome}: [1] - Facil'
[2] - Médio
[3] - Dificil: '''))
if nivel == 1:
    print('Olá... pensei em um numero entre 0 e 10 tente acertar!')
    computador = randint(1, 10)
    acertou = False
    palpites = 0
    while not acertou:
        jogador = int(input('Qual seu palpite? '))
        if jogador == computador:
            acertou = True
            palpites += 1
        if jogador < computador:
            print('Um pouco mais')
            palpites += 1
        if jogador > computador:
            print('Um pouco menos')
            palpites += 1
    print(f'Fim, você acertou com {palpites} palpites o numero que pensei foi {computador}.')
if nivel == 2:
    computador = randint(0, 10)
    acertou = False
    palpites = 0
    print('Bem vindo ao nivel médio você tem 3 chances de acertar o numero em que pensei entre 0 e 10!\nQUE COMEÇEM '
          'OS JOGOS')
    while not acertou:
        jogador = int(input('Em que numero você acha que pensei ?'))
        if jogador == computador:
            acertou = True
            palpites += 1
            print(f'Parábens você acertou com {palpites} palpites o numero que pensei foi {computador}')
        if jogador < computador:
            print('Um pouco mais!')
            palpites += 1
        if jogador > computador:
            print('Um pouco menos')
            palpites += 1
        if palpites > 2:
            print(f'Acabou suas tentativas jogue novamente! O numero que pensei foi {computador}')
            acertou = True

if nivel == 3:

    while c == 's':
        computador = randint(0, 10)
        jogador = int(input('Vamos começar escolha um numero entre 0 e 10 : '))  # jogador tenta adivinhar
        while jogador not in range(0, 10):
            jogador = int(input('Opa, não entendi coloque de novo sua escola de 0 a 10: '))
        print('-*-' * 20)
        print('Lendo seu pensamento...')
        sleep(1.5)
        if jogador == computador:
            sleep(0.7)
            print('Droga, você ganhou de mim')
            contador += 1
            sleep(0.7)
        else:
            sleep(0.7)
            print(f'Sabia que você ia errar eu pensei no numero {computador}')
            contadorpc += 1
            sleep(0.7)

        print('-*-' * 20)
        print(f'O placar está {contador} para você e {contadorpc} para mim')
        print('-*-' * 20)
        sleep(1)
        c = str(input('Para jogar novamente Tecle -(S)\nPara Desistir Tecle-(n)')).lower()
    if contadorpc > contador:
        print('==' * 20)
        print(f'Até mais {nome},foi um prazer ganhar de você kkkk')
        print('==' * 20)
    else:
        print('==' * 20)
        print(f'Até mais {nome}, volte de novo que ganharei de você')
        print('==' * 20)
