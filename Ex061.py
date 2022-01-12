print('{:=^60}'.format('DESAFIO 061'))
a1 = int(input('insira o primeiro termo da P.A.: '))
r = int(input('insira a razão da P.A.: '))
print('='*60)
print('Os 10 primeiros termos dessa P.A. são:')
cont = 1
while cont != 11:
    print('termo {} → {}'.format(cont, a1))  # símbolo da setinha : alt + 26(no teclado nmérico)
    a1 += r
    cont += 1
print('='*60)