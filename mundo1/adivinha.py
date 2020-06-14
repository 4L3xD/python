from random import randint

computador = randint(0, 10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Advinhe o número: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tentei outra vez.')
        elif jogador > computador:
            print('Menos... Tente outra vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
