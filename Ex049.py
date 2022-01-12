print('{:=^60}'.format(' DESAFIO 049 '))
num = int(input('Insira um número inteiro para ver a sua tabuada: '))
print('{:^60}'.format('TABUADA DO {}'.format(num)))

for c in range(1,11):
    print('='*60)
    print('{} X {:2} = {}'.format(num, c, num*c))
print('='*60)
