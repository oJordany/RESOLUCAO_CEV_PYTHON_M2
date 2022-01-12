from random import randint
from time import sleep

print('{:=^60}'.format('DESAFIO 045'))
print('{:•^60}'.format(' JOGO DO JOKENPÔ '))

computador = randint(1, 3)
if computador == 1:
    computador = 'PEDRA'
elif computador == 2:
    computador = 'PAPEL'
else:
    computador = 'TESOURA'
res = 'S'
while res == 'S':
    res = ''
    jogador = str(input('ESCOLHA PEDRA/PAPEL/TESOURA: ')).strip().upper()
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!')
    print('=-'*30)
    if jogador == 'PEDRA' and computador == 'PEDRA':
        print('EU = {}  X  VOCÊ = {}'.format(computador, jogador))
        print('O JOGO EMPATOU ☺')
        print('=-' * 30)
    elif jogador == 'PEDRA' and computador == 'PAPEL':
        print('EU = {}  X  VOCÊ = {}'.format(computador, jogador))
        print('VOCÊ PERDEU:( EU GANHEI O JOGO ☻')
        print('=-' * 30)
    elif jogador == 'PEDRA' and computador == 'TESOURA':
        print('EU = {}  X  VOCÊ = {}'.format(computador, jogador))
        print('PARABÉNS☺! VOCÊ GANHOU DE MIM :(')
        print('=-' * 30)
    elif jogador == 'TESOURA' and computador == 'TESOURA':
        print('EU = {}  X  VOCÊ = {}'.format(computador, jogador))
        print('O JOGO EMPATOU ☺')
        print('=-' * 30)
    elif jogador == 'TESOURA' and computador == 'PEDRA':
        print('EU = {}  X  VOCÊ = {}'.format(computador, jogador))
        print('VOCÊ PERDEU:( EU GANHEI O JOGO ☻')
        print('=-' * 30)
    elif jogador == 'TESOURA' and computador == 'PAPEL':
        print('EU = {}  X  VOCÊ = {}'.format(computador, jogador))
        print('PARABÉNS☺! VOCÊ GANHOU DE MIM :(')
        print('=-' * 30)
    elif jogador == 'PAPEL' and computador == 'PAPEL':
        print('EU = {}  X  VOCÊ = {}'.format(computador, jogador))
        print('O JOGO EMPATOU ☺')
        print('=-' * 30)
    elif jogador == 'PAPEL' and computador == 'TESOURA':
        print('EU = {}  X  VOCÊ = {}'.format(computador, jogador))
        print('VOCÊ PERDEU:( EU GANHEI O JOGO ☻')
        print('=-'*30)
    elif jogador == 'PAPEL' and computador == 'PEDRA':
        print('EU = {}  X  VOCÊ = {}'.format(computador, jogador))
        print('PARABÉNS☺! VOCÊ GANHOU DE MIM :(')
        print('=-'*30)
    else:
        print('INSIRA UMA OPÇÃO VÁLIDA...')
        res = str(input('QUER TENTAR DE NOVO?\nRES[S/N]: ')).upper().strip()
        print('•'*60)
