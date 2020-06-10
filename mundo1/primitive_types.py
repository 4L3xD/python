n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
print('A soma vale ', s)

# str
n1 = (input('\nDigite um valor para verificarmos seu tipo: '))
print(type(n1))

n1 = (input('\nDigite um valor: '))
n2 = (input('Digite outro valor: '))
s = n1+n2
# print('Concatenação entre', n1, 'e', n2, 'é', s)
print('Concatenação entre {} e {} é {}'.format(n1, n2, s))

n = input('\nDigite algo: ')
print('isalnum? ', n.isalnum())
print('isalpha? ', n.isalpha())
print('isascii? ', n.isascii())
print('isdecimal? ', n.isdecimal())
print('isspace? ', n.isspace())
print('está capitalizada? ', n.istitle)