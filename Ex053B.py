frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('A frase invertida é : {}'.format(inverso))
if inverso == junto:
    print('Portanto, temos um palíndromo!')
else:
    print('Portanto, não é um palíndromo')