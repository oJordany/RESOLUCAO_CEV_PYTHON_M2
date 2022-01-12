print('{:=^60}'.format(' DESAFIO 071 '))
print('='*60)
print('{:^60}'.format("JORDY'S BANK"))
print('='*60)
saque = int(input('Insira o valor que você quer sacar: R$'))
if saque % 50 == 0:
    print(f'Saque: {int(saque/50)} nota(s) de R$50.00')
else:
    if saque > 50:
        print(f'Saque: {saque//50} nota(s) de R$50.00, ', end = '')
        resto = saque - (50*(saque//50))
        if resto % 20 == 0:
            print(f'{int(resto/20)} nota(s) de R$20.00 ', end = '')
        else:
            if resto > 20:
                print(f'{resto // 20} nota(s) de R$20.00, ', end='')
                resto = resto - (20*(resto // 20))
                if resto % 10 == 0:
                    print(f'{int(resto / 10)} nota(s) de R$10.00 ', end='')
                else:
                    if resto > 10:
                        print(f'{resto // 20} nota(s) de R$10.00, ', end='')
                        resto = resto - (10*(resto // 10))
                        print(f'{resto} nota(s) de R$1.00')
                    else:
                        print(f'{resto} nota(s) de R$1.00')
            else:
                if resto % 10 == 0:
                    print(f'{int(resto / 10)} nota(s) de R$10.00 ', end='')
                else:
                    if resto > 10:
                        print(f'{resto // 10} nota(s) de R$10.00, ', end='')
                        resto = resto - (10*(resto // 10))
                        print(f'{resto} nota(s) de R$1.00')
                    else:
                        print(f'{resto} nota(s) de R$1.00')
    else:
        if saque % 20 == 0:
            print(f'Saque: {int(saque/20)} nota(s) de R$20.00 ', end = '')
        else:
            if saque > 20:
                print(f'Saque: {saque // 20} nota(s) de R$20.00, ', end='')
                resto = saque - (20*(saque // 20))
                if resto % 10 == 0:
                    print(f'{int(resto / 10)} nota(s) de R$10.00 ', end='')
                else:
                    if resto > 10:
                        print(f'{resto // 10} nota(s) de R$10.00, ', end='')
                        resto = resto - (10*(resto // 10))
                        print(f'{resto} nota(s) de R$1.00')
                    else:
                        print(f'{resto} nota(s) de R$1.00')
            else:
                if saque % 10 == 0:
                    print(f'Saque: {int(saque / 10)} nota(s) de R$10.00 ', end='')
                else:
                    if saque > 10:
                        print(f'Saque: {saque // 10} nota(s) de R$10.00, ', end='')
                        resto = saque - (10*(saque // 10))
                        print(f'{resto} nota(s) de R$1.00')
                    else:
                        print(f'Saque: {saque} nota(s) de R$1.00')
