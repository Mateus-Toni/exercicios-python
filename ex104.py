def leiaInt(msg=''):
    """
    -> Valida entradas numéricas do tipo inteiro.
    :param msg: (opcional) Mensagem que será exibida na tela para entrada do valor numérico.
    :return: O valor numérico recebido como caracter transformado em inteiro.
    """
    print('\n', '-' * 30, sep='')
    while True:
        num = input(msg)
        if num.replace('-', '', 1).isdigit():  # .isnumeric()
            return int(num)
            break
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')

