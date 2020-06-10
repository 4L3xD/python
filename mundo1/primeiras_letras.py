combate = str(input('Rampa ou arma? ')).strip()
print(combate[:5].upper() == 'RAMPA' or combate[:4].upper() == 'ARMA')

nome = str(input('Rampa ou arma? ')).strip()
print('{}'.format('arma' in combate.lower()))