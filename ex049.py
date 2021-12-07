tabuada = int(input('Digite qual tabuada você quer saber: '))
fimtabuada = int(input('Até quanto: '))
for multiplo in range(0, fimtabuada + 1):
    print(f'{tabuada}x{multiplo} = {tabuada * multiplo}')