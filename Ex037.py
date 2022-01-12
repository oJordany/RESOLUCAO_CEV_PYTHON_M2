print('{:=^60}'.format('DESAFIO 037'))
print('{:=^60}'.format('CONVERSOR DE BASES DECIMAIS'))
num = int(input('Insira um número inteiro para ser convertido: '))

print('_'*61)
print('{:<60}{}'.format('|[1] para converter para binário', '|'))
print('{:<60}{}'.format('|[2] para converter para octal', '|'))
print('{:<60}{}'.format('|[3] para converter para hexadecimal', '|'))
print('_'*61)

escolha = int(input('Escolha a sua base de conversão: '))
print('-'*60)

if escolha == 1:
    print('O número {} é igual a {} em binário'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('O número {} é igual a {} em octal'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O número {} é igual a {} em hexadecimal'.format(num, hex(num)[2:]))
else:
    print('opção inválida, tente novamente...')
print('='*60)
