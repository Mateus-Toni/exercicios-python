import random
num_pc = random.randint(0, 5)
num_p = int(input('Digite um número: '))
if num_pc == num_p:
    print('você venceu')
else:
    print('você perdeu')
print(num_pc)