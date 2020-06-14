print('Gerador de progressão aritmética')
print('-=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    mais = int(input('\nQuantos termos você quer mostrar a mais? '))
print('Mostrados {} termos da progressão.'.format(total))
