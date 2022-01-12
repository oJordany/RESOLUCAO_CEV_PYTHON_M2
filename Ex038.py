print('{:=^60}'.format('DESAFIO 038'))
print('{:^60}'.format('COMPARADOR DE NÚMEROS'))
n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
print('='*60)
if n1 > n2 :
    print('O primeiro valor é maior')
elif n2 > n1 :
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')
print('='*60)
