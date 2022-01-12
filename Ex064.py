print('{:=^60}'.format(' DESAFIO 064 '))
print('O PROGRAMA SÓ PARA QUANDO O NÚMERO 999 É DIGITADO')
S = 0
qntdnum = 0
num = 0
while num != 999:
    num = int(input('Insira um valor inteiro qualquer: '))
    if num != 999:
        S += num
        qntdnum += 1
print('='*60)
print('FORAM DIGITADOS {} NÚMEROS E A SOMA DELES É IGUAL A {}'.format(qntdnum,S))
