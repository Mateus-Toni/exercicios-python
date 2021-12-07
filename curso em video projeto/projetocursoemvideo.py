import defsprojeto

while True:
    defsprojeto.cabecalho('Menu Principal')
    defsprojeto.menu('ver pessoas cadastradas', 'cadastrar nova pessoa', 'sair do sistema')
    try:
        opc = int(input('Escolha uma opção: '))
    except:
        print('Digite um número válido')
    else:
        if opc == 1:
            defsprojeto.mostrarpessoas('r+', 'PESSOAS.txt')
        elif opc == 2:
            defsprojeto.cadastro('a+', 'PESSOAS.txt')
        elif opc == 3:
            break
        else:
            print('Opção inválida')
