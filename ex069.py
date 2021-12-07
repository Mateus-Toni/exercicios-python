nc = maior = menor = m = 0
while True:
    nc += 1
    print('-==-'*6)
    print(f' Cadastro da {nc} pessoa')
    print('-==-' * 6)
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo: [M/F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        while sexo != 'M' and sexo != 'F':
            sexo = str(input('Tente de novo: Digite o seu sexo: [M/F]')).upper()
    q = str(input('Quer continuar? [S/N]')).upper()
    if q != 'S' and q != 'N':
        while q != 'S' and q != 'N':
            q = str(input('Tente de novo: Quer continuar? [S/N]')).upper()
    if idade >= 18:
        maior += 1
    if idade < 20 and sexo == 'F':
        menor += 1
    if sexo == 'M':
        m += 1
    if q == 'N':
        break
if maior > 1 and menor > 1 and m > 1:
    print(f'Foram cadastradas {maior} pessoas com mais de 18 anos.')
    print(f'Foram cadastrados {m} homens.')
    print(f'Foram cadastradas {menor} mulheres com menos de 20 anos.')
elif maior < 2 and menor < 2 and m < 2:
    print(f'Foi cadastrado {maior} pessoa maior de 18 anos.')
    print(f'Foi cadastrado {m} homem.')
    print(f'Foi cadastrada {menor} mulher com menos de 20 anos.')
