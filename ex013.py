sal = float(input('Digite o salário sem aumento: R$'))
aum = int(input('Digite a porcentagem do aumento: '))
print(f'O salário de R${sal} com {aum}% de aumento passa a ser R${sal + (sal * aum / 100)}')