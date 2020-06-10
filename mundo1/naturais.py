print('Números Naturais (N) \n N = { ∃ a, b, c, ..., ∞. ∀ a, b ^ c ∈ N a+1 = b, b+1 = c | b é sucessor de a, c é sucessor de b, ... } \n N = { 0, 1, 2, 3, ..., ∞ } \n 0 é o Elemento Neutro ⊂ N | ∀ n ∈ N, n+0 = n')

natural = False

while natural == False:
    n = int(input('\nDigite um número \033[31mNatural\033[m: '))
    if n >= 0:
        natural = True

if n == 0:
    print('\nO antecessor de {} é \033[31m{}\033[m e não pertence ao conjuntos dos Naturais. \nO sucessor de {} é \033[31m{}\033[m.'.format(n, (n-1), n, (n+1)))
else:
    print('\nO antecessor de {} é \033[31m{}\033[m e o sucessor de {} é \033[31m{}\033[m.'.format(n, (n-1), n, (n+1)))

if n == 0:
    print('{} é um elemento Neutro. Não é par ou ímpar!'.format(n))
elif n%2 == 0:
    print('{} é par!'.format(n))
else: 
    print('{} é impar!'.format(n))

print('O Dobro de \033[32m{}\033[m é igual a \033[34m{}\033[m, \nO quadrado de \033[32m{}\033[m é \033[34m{}\033[m, \nA raíz de \033[32m{}\033[m equivale a \033[34m{:.2f}\033[m.'.format(n, (n*2), n, (n**2), n, (n**(1/2))))