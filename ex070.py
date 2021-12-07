# ex70 pede nome e preco de produtos e ve quanto voce pagou, qnts passaram de R$:1000 e o, ou os mais baratos :3
s = qnt = n = mpreco = 0
plural = ['Os', 'produtos', 'baratos', 'foram:', 'custaram']
singular = ['O', 'produto', 'barato', 'foi:', 'custou']  # Definindo variaveis que nao variam sempre
frase = singular
while True:
    # definindo variaveis que mudam constantemente
    nome = preco = ""
    cnt = ""
    while nome == "":  # se vazio repita
        nome = input('Digite o nome do produto: ').strip()
    while preco == "":  # se vazio repita
        preco = input('Preco R$:')
    preco = float(preco)
    while cnt not in "SsNn" or cnt == "":
        cnt = input('Quer continuar? [S/N]')
        if cnt != "":
            cnt = cnt[0]  # se continuar nao for vazio, pegue a 1 letra (se vazio da erro)
    n += 1  # quantos produtos digitados
    s += preco  # somando  o preco dos produtos
    if preco > 1000:
        qnt += 1  # soma se preco > 1000
    if n == 1:  # pegando o nome e valor do 1 produto
        mpreco = preco
        mbarato = nome
    elif preco < mpreco:
        frase = singular
        mpreco = preco
        mbarato = nome
    elif preco == mpreco and mbarato.find(nome) == -1:  # se n for 1 prod e o preco for igual o menor preco:
        # caso esse produto ja tenha sido add nao addicione dnv
        mbarato = [mbarato, nome]  # o mais barato sera uma lista com esses valores
        frase = plural  # as frases ficaram no plural
        mbarato = ', '.join(mbarato)  # junte a lista "mais barato" em uma so string com ", " entre os itens
    if cnt in "Nn" and cnt != "":  # se continuar == nao feche o preograma
        print('-Fim-')
        break
print(f'\nVc gastou R${s:.2f}!')  # mostrando a soma dos produtos
print(f'Ao todo, voce comprou {qnt} produtos por mais de R$:1000,00 cada!')  # Mostrando qnts passaram de 1000
print(f'{frase[0]} {frase[1]} mais {frase[2]} {frase[3]} {mbarato} que {frase[4]} R$:{mpreco:.2f}!')
