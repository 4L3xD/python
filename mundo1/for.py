for cont in range(10, -1, -1):
    print(cont)
print('Bum! Bum! BUM!')

for i in range(5, 1, -2):
    print(i)
print('ínicio 5 até 1 a cada 2 elementos em ordem descrescente.')

# mesma linha
for n in range(2, 51, 2):
    print(n, end= ' ')
print('Tcharam!')

for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end= ' ')
print('É isso ai...')

cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # contador
        soma = soma + c # acumulador
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont+= 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))

soma = 0
for i in range(2, 13, 2):
    print(i)
    soma += i
print('A respostas é: {}'.format(soma))

