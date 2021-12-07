from random import choice
#Gerando a palavra do jogo:
file = open('jogodaforca.txt','r',encoding='utf-8')
palavras = str(file.readline()).split()
forca = str(choice(palavras)).upper()

#cabeçalho:
print('='*30)
print('         JOGO DA FORCA')
print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
print(f'A palavra tem {len(forca)} letras')
print('_ '*len(forca))
print('='*30)

#variáveis e listas que usei:
erros = list()
acertos = list()
jdigitado = list()
erro = cont = 0

#aqui gerei aquela parte onde vai ficar os acertos:
for c in range(len(forca)):
    acertos.append('_')

#estrutura do jogo:
while True:
    letras_acertadas = 0
    chute = str(input('Digite uma letra: ')).upper()
    #teste para o usuário nao repetir a letra que ele ja chutou:
    if chute not in erros and chute not in acertos:
        #caso usuário acerte:
        if chute in forca:
            print('acertou ',end='')
            for controle_1 in range(len(forca)):
                if chute == forca[controle_1]:
                    acertos[controle_1] = chute
                    letras_acertadas += 1
            if letras_acertadas > 1:
                print(f'{letras_acertadas} letras')
            else:
                print(f'{letras_acertadas} letra')
            for controle_2 in acertos:
                print(f'{controle_2} ',end='')
            print()
            print('=' * 30)
            letras_acertadas = 0
        #caso usuário tenha errado:
        else:
            cont += 1
            erro += 1
            print('=' * 30)
            print(f'errou pela {erro}o vez')
            erros.append(chute)
            print('Seus erros ->',end=' ')
            for controle_4 in erros:
                print(f'{controle_4} ',end='')
            print()
            print('=' * 30)
        if  forca == ''.join(acertos):
            print('Parabénnss, você acertou a palavra!!!!!')
            break
        elif cont == 10:
            print('''
  +---+
  |   |
  O   |
 /|\  | 
 / \  |
      |
=========''')
            print('Infelizmente você perdeu =(\nTente de novo!')
            break
    else:
        print('Você ja digitou essa letra!!')







