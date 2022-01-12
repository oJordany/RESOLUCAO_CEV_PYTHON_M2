print('{:=^60}'.format(' DESAFIO 050 '))
lista = [0,0,0,0,0,0]
sp = 0
cont = 0
for c in range(1, 7):
    clista = c - 1
    n = int(input('insira o {}º número: '.format(c)))
    lista[clista] = n
    if n%2 == 0:      #caso o número inserido na lista seja par
        cont += 1
        sp += n
print('Números digitados : {}'.format(lista))
print('Quantidade de números pares: {}'.format(cont))
print('Soma dos números pares digitados : {}'.format(sp))
