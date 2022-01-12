print('{:=^60}'.format(' DESAFIO 055 '))
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Peso(Kg) da {} pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
print('='*60)
