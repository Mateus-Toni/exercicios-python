def maior(*num):
    if len(num) > 0:
        print(f'O maior de {num} é o {max(num)}.')
    else:
        print('Não foi informado nenhum valor!')
maior(9, 2, 11, 5, 3)
maior(4, 7, 1, 2)
maior(1, 2, 3, 7, 3, 9, 5, 12)
maior(6)
maior(1, 2)
maior()