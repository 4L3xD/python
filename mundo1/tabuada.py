num = int(input('Digite um número Z: '))

for multiplo in range(11):
    print('{} * {} = {}'.format(num, multiplo, (num*multiplo)))
   # multiplo += 1 iteração na própria função for