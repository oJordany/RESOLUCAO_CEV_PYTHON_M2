print('{:=^60}'.format(' DESAFIO 046 '))
import emoji
from time import sleep

for c in range(10,-1,-1):
    print('{:^60}'.format(c))
    sleep(1)
print('{:^60}'.format(emoji.emojize(":confete: :cone_de_festa: :brilhos: POOWW :brilhos: :cone_de_festa: :confete:", language = 'pt')))
print('='*60)