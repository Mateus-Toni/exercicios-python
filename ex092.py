from datetime import datetime, date

ano = str(date.today())[0:4]


def s():
    print('-' * 40)


lista = []

while True:
    s()
    reg_trabalhador = {'nome': str(input('Qual o seu nome? ')).upper(),
                       'idade': int(input('Idade: ')),
                       'sexo': str(input('Sexo [F/M]: ')).upper()[0]}
    while True:
        if reg_trabalhador['idade'] < 16:
            s()
            if reg_trabalhador['sexo'] == 'F':
                print(
                    f'A {reg_trabalhador["nome"]} não pode ter carteira de trabalho. Somente quando chegar a 16 anos de idade')
                break
            else:
                s()
                print(
                    f'O {reg_trabalhador["nome"]} não pode ter carteira de trabalho. Somente quando chegar a 16 anos de idade')
                break
        reg_trabalhador['ctps'] = int(input('Qual n° carteira? [Se não tem digite 0] '))
        if reg_trabalhador['ctps'] == 0:
            if reg_trabalhador['sexo'] == 'F':
                print(
                    f'A Sra. {reg_trabalhador["nome"]} se dirija ao poupa tempo mais próximo e providencie a sua. Até a próxima.')
            else:
                print(
                    f'O Sr. {reg_trabalhador["nome"]} se dirija ao poupa tempo mais próximo e providencie a sua. Até a próxima.')
        else:
            reg_trabalhador['ano_contratacao'] = int(input('Ano de contratação: '))
            reg_trabalhador['salario'] = float(input('Qual valor de salário: '))
            reg_trabalhador['aposentadoria'] = ' '

            s()
            for chave, valor in reg_trabalhador.items():
                if reg_trabalhador['sexo'] in 'M':
                    reg_trabalhador['aposentadoria'] = 65 - (int(ano) - reg_trabalhador['ano_contratacao'])
                else:
                    reg_trabalhador['aposentadoria'] = 60 - (int(ano) - reg_trabalhador['ano_contratacao'])
                print(f'O {chave} tem o valor {valor}')
        lista.append(reg_trabalhador)
        del reg_trabalhador
        break
    s()
    continuar = str(input('Quer continuar? [S/N] '))[0]
    if continuar in 'Nn':
        break
s()
print('Ate aqui finalizado')
s()
print(lista)

