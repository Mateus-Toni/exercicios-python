km = float(input('Qual a distância em (Km) você deseja percorrer? '))
if km <= 200:
    print('Sua passagem vai custar {} reais. '.format(km * 0.5))
else:
    print('Sua passagem vai custar {} reais. '.format(km * 0.45))
