print('{:=^60}'.format('DESAFIO 062'))
a1 = int(input('insira o primeiro termo da P.A.: '))
r = int(input('insira a razão da P.A.: '))
print('='*60)
print('Os 10 primeiros termos dessa P.A. são:')
cont = 1
fim = 0
res = 10
while res != 0:
    fim = fim + res
    while cont <= fim:
        print('termo {} → {}'.format(cont, a1))  # símbolo da setinha : alt + 26(no teclado nmérico)
        a1 += r
        cont += 1
    print('='*60)
    res = int(input('Quantos termos a mais você quer ver? : '))
