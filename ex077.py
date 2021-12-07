exemplo = ('bumbum', 'biluteteia', 'caveleiros')
for palavra in exemplo:
    print(f'na palavra {palavra.upper()} temos: ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print()
