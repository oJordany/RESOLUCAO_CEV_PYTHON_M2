print('{:=^60}'.format(' DESAFIO 048 '))
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
    print(c)
print('''A soma entre todos os {} valores solicitados é \033[1;34m{}\033[m. '''.format(cont, s))
print('='*60)
