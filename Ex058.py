print('{:=^60}'.format('DESAFIO 058'))
print('{:-^60}'.format('JOGO DA ADIVINHAÇÃO'))
from random import randint
from time import sleep
computador = randint(0, 10) #faz o computador "PENSAR"
print("-=-" *20)
print('Vou pensar em um número entre 0 e 10, tente adivinhar...')
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
fim = False
jogadas = 0
while fim == False:
    print("-=-" * 20)
    jogadas += 1
    if computador == jogador:
        print('PROCESSANDO...')
        sleep(3)
        print('PARABÉNS! VOCÊ CONSEGUIU ACERTAR EM {} JOGADA(S)!'.format(jogadas))
        fim = True
    elif computador > jogador:
        print('PROCESSANDO...')
        sleep(3)
        print('UM POUCO MAIOR...', end = ' ')
        print('TENTE MAIS UMA VEZ.')
        jogador = int(input('Em que número eu pensei? '))  # jogador tenta adivinhar
    elif computador < jogador:
        print('PROCESSANDO...')
        sleep(3)
        print('UM POUCO MENOS...', end=' ')
        print('TENTE MAIS UMA VEZ.')
        jogador = int(input('Em que número eu pensei? '))  # jogador tenta adivinhar
