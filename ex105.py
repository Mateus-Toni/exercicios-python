def notas(* nts, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nts: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situacão da turma
    """
    dicionario = dict()
    dicionario['quantidade'] = len(nts)
    cont = 0
    for c in range(0, len(nts)):
        cont += nts[c]
        if c == 0:
            dicionario['maior'] = nts[c]
            dicionario['menor'] = nts[c]
        else:
            if nts[c] > dicionario['maior']:
                dicionario['maior'] = nts[c]
            if nts[c] < dicionario['menor']:
                dicionario['menor'] = nts[c]
    dicionario['media'] = cont / len(nts)
    if sit:
        if dicionario['media'] >= 7:
            dicionario['situacao'] = 'BOA'
        elif dicionario['media'] >= 5:
            dicionario['situacao'] = 'RAZOÁVEL'
        else:
            dicionario['situacao'] = 'RUIM'
    return dicionario


print(notas(5.5, 9.5, 10, 6.5, sit=True))
help(notas)