from time import sleep
print('{:=^60}'.format('DESAFIO 059'))
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
maior = 0
print('='*60)
escolha = 0
while escolha != 5 :
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    escolha = int(input('Escolha uma opção: '))
    print('='*60)

    if escolha == 1:
        print('{} + {} = {}'.format(v1,v2,v1+v2))
        print('=' * 60)
    elif escolha == 2:
        print('{} x {} = {}'.format(v1, v2, v1 * v2))
        print('=' * 60)
    elif escolha == 3:
        maior = v1
        if v2 > v1:
            maior = v2
        print('Entre {} e {}, o maior valor é {}'.format(v1, v2,maior))
        print('=' * 60)
    elif escolha == 4:
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valor: '))
        print('=' * 60)
    elif escolha == 5:
        print('Programa finalizado')
    else:
        print('Digite uma opção válida')
        escolha = 4
    sleep(2)