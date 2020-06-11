n = input('Digite um número com uma casa de milhar, centenha, dezena e unidade: ').strip()
par = False

milhar = n[0]
centena = n[1]
dezena = n[2]
unidade = n[3]

if int(n) % 2 == 0:
    print('{} é par.\nDivisível por 2.'.format(n))
    par = True

    if int(n) % 4 == 0:
        produto_4 = int(dezena) * 10 + int(unidade) * 1
        if produto_4 % 4 == 0 or produto_4 == 00:
            print('{} é divisível por 4.'.format(n))
            print('dezena: {}, unidade: {}.'.format(dezena, unidade))

    if int(centena) % 2 == 0:
        if int(unidade + dezena + centena) % 8 == 0 or int(unidade + dezena + centena) == 000:
            print('Divisível por 8 com centena par.')
    else:
        produto_8 = int(dezena + unidade) + 4
        if produto_8 % 8 == 0:
            print('Divisível por 8 com centena ímpar.')

    if unidade == '0':
        print('Divisível por 10.') 

if int(unidade + dezena + centena + milhar) % 3 == 0:
    print('Divisível por 3.')
    if par == True:
        print('Divisível por 6.')

if par == False:
    if unidade == '0' or unidade == '5':
      print('Divisível por 5.')
   
    produto_7 = (int(centena) * 100 + int(dezena) * 10 - (2 * int(unidade)))
    if produto_7 % 7 == 0:
        print('Divisível por 7.')

    if int(unidade + dezena + centena + milhar) % 9 == 0:
        print('Divisível por 9.')
    
    #Estudar algoritmo de divisão por 11
    impares = []
    pares = []
    for posicao in range(4):
        numero = (n[posicao])
        if int(numero) % 2 == 1:
            impares.append(numero)
        else: pares.append(numero)
    soma_impares = 0
    soma_pares = 0
    for impar in range(len(impares)):
        soma_impares += int(impares[impar])
    for par in range(len(pares)):
        soma_pares += int(pares[par])
    produto_11 = soma_pares - soma_impares
    if produto_11 % 11 == 0:
        print('Divisível por 11. Soma de pares: {} e soma de ímpares: {}.'
        .format(soma_pares, soma_impares))
    print('Números pares: {}.'.format(pares))
    print('Números impares: {}'.format(impares))
    # Concluir algoritmo!