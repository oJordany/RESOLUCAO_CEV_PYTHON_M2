from random import randint
print('{:=^60}'.format('DESAFIO 068'))
v = 0
print('OLÁ, SOU SEU COMPUTADOR, VAMOS JOGAR PAR OU ÍMPAR...')
while True:
    jescolha = input('Escolha PAR ou ÍMPAR [P/I]: ').upper().strip()[0]
    jnum = int(input('Digite um número entre 0 e 10: '))
    pcnum = randint(0,10)
    if jescolha == 'P':
        pcescolha = 'I'
        if (pcnum + jnum)%2 == 0:
            print('='*60)
            print(f'COMPUTADOR: {pcescolha}      VOCÊ: {jescolha}')
            print(f'{jnum} + {pcnum} = {jnum + pcnum}')
            print('PARABÉNS! Você venceu')
            print('='*60)
            v += 1
        else:
            print('=' * 60)
            print(f'COMPUTADOR: {pcescolha}      VOCÊ: {jescolha}')
            print(f'{jnum} + {pcnum} = {jnum + pcnum}')
            print('Você perdeu, QUE PENA!')
            print('=' * 60)
            break
    elif jescolha == 'I':
        pcescolha = 'P'
        if (pcnum + jnum)%2 == 0:
            print('='*60)
            print(f'COMPUTADOR: {pcescolha}      VOCÊ: {jescolha}')
            print(f'{jnum} + {pcnum} = {jnum + pcnum}')
            print('Você perdeu, QUE PENA!')
            print('='*60)
            break
        else:
            print('=' * 60)
            print(f'COMPUTADOR: {pcescolha}      VOCÊ: {jescolha}')
            print(f'{jnum} + {pcnum} = {jnum + pcnum}')
            print('PARABÉNS! Você venceu')
            print('=' * 60)
            v += 1
    else:
        print('Faça uma escolha válida. Tente de novo...\n{}'.format('='*60))
print(f'Você conseguiu me vencer {v} vez/vezes')