from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor entre 0 e 10: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')