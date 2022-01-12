print('{:=^60}'.format('DESAFIO 069'))
m18 = 0
homens = 0
mulheres20 = 0
res = 'S'
while res == 'S':
    idade = int(input('Digite a sua idade: '))
    sexo = input('Digite o seu sexo [M/F]: ').upper().strip()[0]
    if idade > 18:
        m18 += 1
    if sexo == 'M':
        homens += 1
        res = input('Você quer continuar? [S/N]: ').upper().strip()[0]
    elif sexo == 'F':
        if idade < 20:
            mulheres20 += 1
        res = input('Você quer continuar? [S/N]: ').upper().strip()[0]
    else:
        print('Digite uma opção de sexo válida. Tente de novo...')
        res = 'S'
print('='*60)
print(f'Há {m18} pessoa(s) cadastrada(s) com mais de 18 anos\nHá {homens} homem/homens cadastrado(s)\nHá {mulheres20} mulher/mulheres cadastrada(s) com menos de 20 anos')
