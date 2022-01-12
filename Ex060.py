print('{:=^60}'.format('DESAFIO 060'))
num = int(input('Insira um número para descobrir o seu fatorial: '))
fat = 1
print('{}! = '.format(num), end = '')
while num != 1:
    print('{}'.format(num), end= ' x ')
    fat = fat * num
    num -= 1
print('1 = {}'.format(fat))
