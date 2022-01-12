#Exercício para treinar validação de dados
print('{:=^60}'.format('DESAFIO 057'))
sexo = str(input('Insira o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, insira o seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))