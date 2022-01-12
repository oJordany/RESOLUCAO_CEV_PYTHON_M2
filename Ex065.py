print('{:=^60}'.format(' DESAFIO 065 '))
res = 'S'
num = 0
qntdnum = 0
S = 0
maior = 0
menor = 0
while res == 'S':
    num = int(input('Insira um número inteiro qualquer: '))
    qntdnum += 1
    S += num
    if qntdnum == 1:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    res = input('Você quer continuar a digitar valores? [S/N]: ').strip().upper()[0]
print('='*60)
print('A média entre os valores digitados é {:.2f}'.format(S/qntdnum))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior,menor))
