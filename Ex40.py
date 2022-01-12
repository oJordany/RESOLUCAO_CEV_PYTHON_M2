print('{:=^60}'.format('DESAFIO 40'))
n1 = float(input('Insira a primeira nota do aluno: '))
n2 = float(input('Insira a segunda nota do aluno: '))
m = float((n1+n2)/2)
print('='*60)
if m < 5 :
    print('REPROVADO\nmédia = {:.2f}'.format(m))
elif m >= 5 and m < 7:
    print('RECUPERAÇÃO\nmédia = {:.2f}'.format(m))
elif m >= 7:
    print('APROVADO\nmédia = {:.2f}'.format(m))
print('='*60)