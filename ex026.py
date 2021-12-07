nome = str(input('Digite o seu nome: ')).strip().upper()
print(f'A letra "A" aparece : {nome.count("A")} vezes')
print(f'a primeira letra "A" aparece na {nome.find("A") + 1}o posição')
print(f'A última posição de "A" é na {nome[:].rfind("A") + 1} casa')
