#Escreva um programa para aprovar o empréstimo
#bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos
#anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
val = float(input('Qual o valor da casa quevocê deseja comprar? '))
sal = float(input('Quanto você rece por mês? '))
anos = int(input('Em quanto tempo voce prende pagar? (anos): '))
salp = sal*30/100
parcela = val/(anos*12)
if parcela >= salp:
    print('empréstimo negado')
else:
    print('empréstimo aprovado')
