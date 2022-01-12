frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('A frase invertida é : {}'.format(inverso))
if inverso == junto:
    print('Portanto, temos um palíndromo!')
else:
    print('Portanto, não é um palíndromo')