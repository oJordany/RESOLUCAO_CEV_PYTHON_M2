print('{:=^60}'.format('DESAFIO 063'))
print('Quantos termos da sequência de Fibonacci você quer ver?')
n = int(input('R: '))
if n == 1:
    print('{:-^60}'.format('PRIMEIRO TERMO DA SEQUÊNCIA DE FIBONACCI: '))
    print('0')
elif n == 2:
    print('{:-^60}'.format(' 2 PRIMEIROS TERMOS DA SEQUÊNCIA DE FIBONACCI: '))
    print('0 - 1')
elif n > 1:
    print('{:-^60}'.format(' {} PRIMEIROS TERMOS DA SEQUÊNCIA DE FIBONACCI: ').format(n))
    print('0 - 1', end = ' - ')
    i = 0
    ta = 0
    taa = 0
    pt = 1
    while i != n - 2:
        taa = ta
        ta = pt
        pt = ta + taa
        if i == n - 3:
            print(pt)
        else:
            print(pt, end = ' - ')
        i += 1
else:
    print('='*60)
    print('Esse termo não existe')
