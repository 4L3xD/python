start = str(input('Você quer brincar [s/n]? ')).strip().upper()[0]
while start not in 'SsNn':
    start = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
if start in 'Ss':
    print('Vamos lá!')
if start in 'Nn':
    print('Nos vemos por aí!')