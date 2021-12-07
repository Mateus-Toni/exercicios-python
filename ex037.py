num = int(input('Digite um número inteiro: '))
print('Escolha uma base de conversão: \n [1] converter para Binário \n [2] converter para Octal \n [3] converter para '
      'Hexadecimal')
opcao = int(input('Escolha a opção: '))
b = bin(num).replace('0b', '')
o = oct(num).replace('0o', '')
h = hex(num).replace('0x', '').upper()

if opcao == 1:
    print('{} convertido para Binário é igual a: {}'.format(num, b))
elif opcao == 2:
    print('{} convertido para Octal é igual a: {}'.format(num, o))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual a: {}'.format(num, h))
else:
    print('Você não escolheu uma das opções.')
