import datetime

# ano atual
ano = datetime.date.today().year
print('-'*20)

# ano de nascimento do usuário
nasc = int(input('Em que ano você nasceu? '))
print('-'*20)

# idade do usuário
idade = ano - nasc


# usuário que ainda não esta no ano de alistamento
if idade < 18:
    print('-' * 20)
    print('Ainda faltam {} anos para voce se alistar'.format(18 - idade))
    print('-' * 20)


# usuário que passou da data de alistamento
elif idade > 18:
    print('-' * 20)
    print('Passou a hora do seu alistamento')
    print('Seu alistamento foi a {} anos atrás'.format(ano - nasc))
    print('-' * 20)


# usuário que está no ano de alistamento
else:
    print('-' * 20)
    print('Você esta no seu ano de alistamento')
    print('entre no site do exécito: ' 
          'https://alistamento.eb.mil.br/')
    print('-' * 20)