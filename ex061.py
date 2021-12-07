primeiro_termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

pa = primeiro_termo + (10 - 1)*razao
while primeiro_termo != pa:
    print(f'{primeiro_termo}', end=' → ')
    primeiro_termo = primeiro_termo + razao

print('Fim', end=' ')
