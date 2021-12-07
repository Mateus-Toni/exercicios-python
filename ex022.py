nome = input('digite seu nome: ')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
nomes = nome.split()
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(nomes[0], len(nomes[0])))

