print('{:=^60}'.format(' DESAFIO 053 '))
frase = str(input('Escreva uma frase : ')).upper().strip()
lista = list(''.join(frase.split()))
qtd_letras = len(lista)
con = 0
fim = qtd_letras
for c in range(0, qtd_letras):
    inicio = c
    fim = fim - 1
    if lista[inicio] == lista[fim]:
        con += 1
if con == qtd_letras :
    print('a frase {} \033[1;31mé um palíndromo\033[m'.format(frase))
else:
    print('a frase {} \033[1;31mnão é um palíndromo\033[m'.format(frase))
print('='*60)