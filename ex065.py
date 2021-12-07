num = int
lista = []
continuar = ''
while continuar != 'N':
    num = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    lista += [num]
cont = len(lista)
media = sum(lista) / len(lista)
maior = max(lista)
menor = min(lista)
print(f'Você digitou {cont} números e a média foi {media:.2f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}')
