print('{:=^60}'.format(' DESAFIO 054 '))
from datetime import date
atingiram = 0
natingiram = 0
for c in range(1,8):
    nasc = int(input('Insira o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = date.today().year - nasc
    if idade >= 21:
        atingiram += 1
    else:
        natingiram += 1
print('{} pessoa(s) atingiu/atingiram a maioridade e {} ainda não'.format(atingiram, natingiram))
print('='*60)