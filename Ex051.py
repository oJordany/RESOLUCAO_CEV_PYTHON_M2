print('{:=^60}'.format(' DESAFIO 051 '))
a1 = int(input('insira o primeiro termo da P.A.: '))
r = int(input('insira a razão da P.A.: '))
print('='*60)
print('Os 10 primeiros termos dessa P.A. são:')
a = 0
for c in range(a1, a1 + r*10, r):
    a += 1
    print('termo {} → {}'.format(a,c))  #símbolo da setinha : alt + 26(no teclado nmérico)
print('='*60)