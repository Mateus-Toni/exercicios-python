num = list()
while True:
    num.append(int(input('Valor: ')))
    r = str(input('resp: '))
    if r in 'nN':
        break
print('Foram digitados {} valores'.format(len(num)))
num.sort(reverse=True)
print(num)
if 5 in num:
    print('numero 5 foi digitado e esta na lista')
else:
    print('o número 5 nao esta na lista')
