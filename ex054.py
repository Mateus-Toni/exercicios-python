from datetime import date
ano = date.today().year

menores = 0
maiores = 0

for c in range(1, 7):
    nasc = int(input('Qual o ano de nascimento da {}o pessoa: '.format(c)))
    idade = ano - nasc
    if idade < 18:
        menores += 1
    else:
        maiores += 1


print(maiores, menores)
























