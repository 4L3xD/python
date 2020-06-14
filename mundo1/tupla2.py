num = (
        int(input('Digite um número: ')),
        int(input('Digite um outro número: ')),
        int(input('Digite mais um outro número: ')),
        int(input('Digite um último número, se não for abusar de sua paciência: '))
      )
print(f'Você digitou os valores {num}')
print(f'O valor 0 apareceu {num.count(0)} vezes')

if 2 in num:
    print(f'O valor 2 apareceu na {num.index(2)+1}ª posição')
else:
    print('O valor 2 não foi digitado.')
print('Os valores pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')