print('{:=^60}'.format('DESAFIO 067'))
while True:
    cont = 1
    num = int(input('Digite o número da tabuada que você quer ver: '))
    if num < 0:
        print('PROGRAMA DE TABUADA ENCERRADO, volte sempre')
        break
    else:
        print('{:=^60}'.format(f' TABUADA DO {num} '))
        while cont <= 10:
            print('{:^60}'.format(f'{num:2} x {cont:2} = {num*cont:2}'))
            cont += 1
        print('='*60)
