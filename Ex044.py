print('{:=^60}'.format('DESAFIO 044'))
print('{:^60}'.format('LOJAS JORDANY'))
preco = float(input('Insira o preço da sua compra --> R$'))
print('='*60)
print('{:^60}'.format('..............................'))
print('{:^60}'.format('|CONDIÇÕES DE PAGAMENTO:     |'))
print('{:^60}'.format('|[1] à vista(dinheiro/cheque)|'))
print('{:^60}'.format('|[2] à vista no cartão       |'))
print('{:^60}'.format('|[3] em até 2x no cartão     |'))
print('{:^60}'.format('|[4] 3x ou mais no cartão    |'))
print('{:^60}'.format('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'))
escolha = int(input('Escolha uma condição de pagamento: '))
print('='*60)
if escolha == 1:
    print('Sua compra de R${:.2f} custará R${:.2f} sem juros'.format(preco, preco-(preco*(10/100))))
elif escolha == 2:
    print('Sua compra de R${:.2f} custará R${:.2f} sem juros'.format(preco, preco-(preco*(5/100))))
elif escolha == 3:
    print('Sua compra será parcelada em {}x de R${:.2f} sem juros'.format(2, preco/2))
    print('Sua compra custará R${:.2f} no total'.format(preco))
elif escolha == 4:
    parcela = int(input('Parcelas: '))
    print('='*60)
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(parcela, (preco + (preco * 20/100))/parcela))
    print('Sua compra de R${:.2f} custará R${:.2f} no total'.format(preco, preco + (preco * 20/100)))
else:
    print('Digite uma condição válida')
print('='*60)
