sexo = int(input('''Qual seu sexo?
[1] HOMEM
[2] MULHER
R: '''))
print('utilize ponto')
peso = float(input('Peso (kg): '))
altura = float(input('Altura (metros):'))
imc = peso / (altura * altura)
# HOMEM
if sexo == 1:
    print('Seu imc {:.1f}'.format(imc))
    # ABAIXO DO PESO
    if imc <= 20.0:
        print('Você está abaixo do peso.\nO imc ideal é entre 21 à 24,9')
    # PESO IDEAL
    elif 21.0 <= imc <= 24.9:
        print('Você está no IMC ideal. Parabéns!')
    # OBSIDADE LEVE
    elif 25.0 >= imc <= 29.9:
        print('Você está com obsidade leve.\nO imc ideal é entre 21 à 24,9')
    # OBSIDADE MODERADA
    elif 30.0 >= imc <= 39.9:
        print('Você está com obesidade moderada.\nO imc ideal é entre 21 à 24,9')
    elif imc >= 40.0:
        print('Você está com obesidade mórbida.\nO imc ideal é entre 21 à 24,9')
# MULHER
elif sexo == 2:
    print('Seu imc {:.1f}'.format(imc))
    # ABAIXO DO PESO
    if imc <= 19.0:
        print('Você está abaixo do peso.\nO imc ideal é entre 20 à 23,9')
    # PESO IDEAL
    elif 20.0 >= imc <= 23.9:
        print('Você está no IMC ideal. Parabéns!')
    # OBSIDADE LEVE
    elif 24.0 >= imc <= 28.9:
        print('Você está com obsidade leve.\nO imc ideal é entre 20 à 23,9')
    # OBSIDADE MODERADA
    elif 29.0 >= imc <= 39.9:
        print('Você está com obesidade moderada.\nO imc ideal é entre 20 à 23,9')
    elif imc >= 40.0:
        print('Você está com obesidade mórbida.\nO imc ideal é entre 20 à 23,9')
