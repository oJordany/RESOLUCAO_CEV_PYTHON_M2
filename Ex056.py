print('{:=^60}'.format(' DESAFIO 056 '))
soma_idade = 0
lista_idade = [0,0,0,0]
MMV = 0
HMV = '---XXX---'
for p in range(1,5):
    print('{:_^60}'.format(' {}ª PESSOA '.format(p)))
    sexo = str(input('Insira o seu sexo [M/F]: ')).strip().upper()
    idade = int(input('Insira a sua idade: '))
    soma_idade += idade
    lista_idade[p - 1] = idade
    nome = str(input('Insira o seu nome: ')).strip().upper()
    if sexo == 'M':
        if idade >= lista_idade[p-1]:
            Midade = idade
            HMV = nome
    elif sexo == 'F':
        if idade < 20:
            MMV += 1
media_idade = soma_idade/4
print('='*60)
print('A média da idade dessas quatro pessoas é {:.2f}'.format(media_idade))
print('O nome do homem mais velho é {} e ele tem {} anos'.format(HMV, Midade))
print('Há {} mulher(es) com menos de 20 anos'.format(MMV))
print('='*60)
