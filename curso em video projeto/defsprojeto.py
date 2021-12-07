def cabecalho(txt):
    print('-' * 50)
    print(txt.center(50))
    print('-' * 50)


def menu(*opc):
    for n, c in enumerate(opc):
        print(f'[{n+1}] - {c}')


def mostrarpessoas(mode='r+', name='PESSOAS.txt'):
    with open(name, mode) as variável:
        for l in variável:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]} anos')


def cadastro(mode='a+', name='PESSOAS.txt'):
    nome = str(input('Digite o nome da pessoa: ')).strip()
    idade = str(input('Digite a idade da pessoas: ')).strip()
    with open(name, mode) as arq:
        arq.writelines(f'{nome};{idade}\n')
