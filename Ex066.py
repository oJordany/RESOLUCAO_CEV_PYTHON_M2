print('{:=^60}'.format('DESAFIO 066'))
cont = s = 0
while True:
    num = int(input('insira um número inteiro qualquer (999 para parar): '))
    if num == 999:
        break
    cont += 1
    s += num
print(f'Você digitou {cont} números e a soma entre todos eles é {s}')
