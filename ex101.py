def votar(idade):
    if idade<16:
        return 'você nao pode votar'
    elif 16 >= idade <= 18:
        return 'voto opcional'
    else:
        return 'voto obrigatório'


# código principal
from datetime import date

ano = date.today().year
anonasc= int(input('Qual o ano do seu nascimento? '))

x = ano - anonasc
print(votar(x))
