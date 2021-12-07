from calendar import isleap
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if isleap(ano):
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')
