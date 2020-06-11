from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' * 20)
jogador = int(input('Chute um valor para a saída a seguir: '))
sleep(3)
if jogador == computador:
    print('Parabéns, você acertou! Eu pensei em {}.'.format(computador))
else:
    print('Eu pensei em {}.'.format(computador))