from datetime import date

print('{:=^60}'.format('DESAFIO 039'))
sexo = input('insira o seu sexo [M/F]: ').upper().strip()

if sexo == 'M':
    ano = int(input('insira o seu ano de nascimento: '))
    anoa = date.today().year
    if (anoa - ano) < 18:
        print('Você tem {} anos e ainda vai se alistar'.format(anoa - ano))
        print('Faltam {} anos para você se alistar'.format(18 - (anoa - ano)))
    elif (anoa - ano) == 18:
        print('Você tem {} anos e está na hora de se alistar'.format(anoa - ano))
    else :
        print('Você tem {} anos e o seu tempo de alistamento já passou há {} ano(s) atrás'.format(anoa - ano,(anoa- ano) - 18), end = '')
        print('. Portanto, você se alistou em {}'.format(anoa - ((anoa - ano) - 18)))
else:
    print('Você não precisa se alistar')
print('='*60)
