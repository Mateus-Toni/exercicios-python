def resumo(valor=0, aumento=10, reducao=5):
    """
    -> Aplica várias funções a um valor monetário e mostra os resultados em uma tabela
    formatados.
    Parâmetros opcionais
    :param valor: Valor ao qual serão aplicada as funções.
    :param aumento: Aumento de porcentagem que será calculado na função aumentar.
    :param reducao: Redução de porcentagem que será calculado na função diminuir.
    :return: Sem retorno
    """
    print('-' * 32)
    print('|', 'RESUMO DO VALOR'.center(28), '|')  # print(f'|{"RESUMO DO VALOR":^30}|')
    print('-' * 32)
    print(f'| Preço analisado |  {moeda(valor):<9} |')
    print(f'| Metade do preço |  {metade(valor, True):<9} |')
    print(f'| Dobro do preço  |  {dobro(valor, True):<9} |')
    print(f'| {aumento:>3}% de aumento |  {aumentar(valor, aumento, True):<9} |')
    print(f'| {reducao:>3}% de redução |  {diminuir(valor, reducao, True):<9} |')
    print('-' * 32)