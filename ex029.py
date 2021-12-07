velo = int(input('Qual a velociadade do carro? : '))
if velo > 80:
    print('voce foi multado e devera pagar um multa de R${:.2f}'.format((velo-80)*7))
else:
    print('você é um bom motorista')