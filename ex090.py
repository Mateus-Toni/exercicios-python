aluno = list()
aluno1 = list()
sala = list()

while True:
    aluno.append(str(input('Digite o nome do aluno: ')))
    aluno.append(float(input('Digite a primeira nota: ')))
    aluno.append(float(input('Digite a segunda nota: ')))
    aluno1.append(aluno[:])
    aluno[1] = (aluno[1]+aluno[2])/2
    aluno.pop(2)
    sala.append(aluno[:])
    aluno.clear()
    resp = str(input('Deseja continuar? '))
    if resp in 'Nn':
        break
print(f'N.chamada       nome:       nota final')
for i,c in enumerate(sala):
    print(f'{i+1}               {c[0]}          {c[1]}')

while True:
    n = int(input('Qual aluno deseja ver? '))
    if n == 999:
        break
    for c in range(3):
        print(f'{aluno1[n][c]}      ', end='')
    print()
link = tuple()

print(link)
