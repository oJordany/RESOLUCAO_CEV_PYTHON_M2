from datetime import date

print('{:=^60}'.format('DESAFIO 041'))
ano = int(input('Insira o ano de nascimento do atleta: '))
anoa = date.today().year

if (anoa - ano) <= 9:
    print('IDADE : {}'.format(anoa - ano))
    print('ATLETA DA CATEGORIA MIRIM')
elif (anoa - ano) <= 14:
    print('IDADE : {}'.format(anoa - ano))
    print('ATLETA DA CATEGORIA INFANTIL')
elif (anoa - ano) <= 19:
    print('IDADE : {}'.format(anoa - ano))
    print('ATLETA DA CATEGORIA JÚNIOR')
elif (anoa - ano) <= 25:
    print('IDADE : {}'.format(anoa - ano))
    print('ATLETA DA CATEGORIA SÊNIOR')
else:
    print('IDADE : {}'.format(anoa - ano))
    print('ATLETA DA CATEGORIA MASTER')
print('='*60)