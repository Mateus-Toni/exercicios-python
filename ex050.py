s = 0
for c in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num%2 == 0:
        s = s + num
print(f'A soma dos números pares informados é {s}.')
