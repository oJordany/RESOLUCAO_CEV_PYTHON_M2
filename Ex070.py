print('{:=^60}'.format(' DESAFIO 070 '))
res = 'S'
cont = maisbarato = precomaisbarato = totgasto = maisde1000 = 0
while res == 'S':
    cont += 1
    nome = input('Digite o nome do produto: ')
    preco = float(input('Insira o preço do produto: R$'))
    totgasto += preco
    if preco > 1000:
        maisde1000 += 1
    if cont == 1:
        maisbarato = nome
        precomaisbarato = preco
    elif preco < precomaisbarato:
        maisbarato = nome
        precomaisbarato = preco
    res = input('Você quer inserir mais produtos? [S/N]: ').upper().strip()[0]
print('='*60)
print(f'O total gasto na compra foi R${totgasto:.2f}\nHá {maisde1000} produto(s) que custa(m) mais de R$1000.00\nProduto mais barato: {maisbarato} → R${precomaisbarato:.2f}')
