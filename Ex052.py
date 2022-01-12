print('{:=^60}'.format(' DESAFIO 052'))
num = int(input('digite um número inteiro qualquer: '))
s = 0
for c in range(1, num + 1):
    if num%c == 0:
        print('\033[1;32m{}\033[m'.format(c), end = ' ')
        s += 1
    else:
        print('\033[1;31m{}\033[m'.format(c), end = ' ')
print('\n\033[1;32mverde\033[m → divisível')
print('\033[1;31mvermelho\033[m → não divisível')
print('=-'*30)
if s == 2:
    print('O número {} é primo'.format(num))
else:
    print('O número {} não é primo'.format(num))
print('='*60)
