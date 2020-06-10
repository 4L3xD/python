from random import choice, shuffle
p1 = str(input('Digite uma palavra:'))
p2 = str(input('Digite uma segunda palavra:'))
p3 = str(input('Digite uma outra palavra:'))
p4 = str(input('Digite uma última palavra:'))

lista = [p1, p2, p3, p4]
escolhido = choice(lista)
print('A palavra escolhida foi {}.'.format(escolhido))

shuffle(lista)
print('Lista de palavras embaralhadas: {}'.format(lista))