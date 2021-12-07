nome = str(input('Digite o nome do aluno: '))
media = float(input('Digite a média do aluno: '))
if media > 7:
    situacao = 'Aprovado'
elif 5 < media <= 7:
    situacao = 'Recuperação'
else:
    situação = 'Reprovado'
dados = {'nome': nome, 'média': media, 'situaçao': situacao}
print(dados['nome'],end=' ')
print(dados['média'],end=' ')
print(dados['situaçao'])
