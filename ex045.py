#Jogo de Pedra-Papel-Tesoura

#Nessa parte o computador vai geral a "arma" dele
import random
lista = ['pedra','papel','tesoura']
pc = random.choice(lista)


#Nessa parte o Jogador faz a escolha
print("""Escolha uma opção: 
[1] Pedra
[2] Papel
[3] Tesoura""")
jogador = int(input('Escolha uma opção:'))


#Aqui vai ser gerado o resultado final.
#Caso jogador escolha pedra:
if jogador == 1:

    jogador = 'pedra'
    if jogador == pc:
        print('EMPATE')
    elif pc == 'papel':
        print('COMPUTADOR GANHOU')
    else:
        print('VOCÊ GANHOU')

#Caso jogador escolha papel:
elif jogador == 2:

    jogador = 'papel'
    if jogador == pc:
        print('EMPATE')
    elif pc == 'tesoura':
        print('COMPUTADOR GANHOU')
    else:
        print('VOCÊ GANHOU')

#Caso jogador escolha tesoura:
elif jogador == 3:

    jogador = 'tesoura'
    if  jogador == pc:
        print('EMPATE')
    elif pc == 'pedra':
        print('COMPUTADOR GANHOU')
    else:
        print('VOCÊ GANHOU')

#Caso ele digite qualquer outra coisa:
else:
    print('Tente de novo')
