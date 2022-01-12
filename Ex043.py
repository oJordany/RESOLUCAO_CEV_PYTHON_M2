from math import pow
print('{:=^60}'.format('DESAFIO 043'))
peso = float(input('Insira o seu peso em Kg: '))
altura = float(input('Insira a sua altura em metros: '))
imc = peso/pow(altura, 2)
print('IMC = {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('Você está com o PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('Você está em situação de SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Você está em situação de OBESIDADE')
else:
    print('Você está em situação de OBESIDADE MÓRBIDA')
print('='*60)
