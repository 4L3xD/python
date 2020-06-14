cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')
while True:
    num = int(input('Digite um número entre 0 e 5: '))
    if 0 <= num <= 5:
        break
    print('Tente novamente com os números corretos.', end='')
print(f'Você digitou o número {cont[num]}')

print(f'Todos os números da tupla {cont}')
print(f'Os 3 primeiros números são {cont[0:3]}')
print(f'Os 2 últimos números são {cont[-2:]}')
print(f'Números em ordem alfabetica: {sorted(cont)}')