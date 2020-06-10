nome = str(input('Digite seu nome comṕleto: ')).strip()
print('Analisando seu nome...\nSeu nome em MAIÚSCULAS é {} e em minúsculas é {}.'
.format(nome.upper(), nome.lower()))
print('Quantidade de letras do seu nome: {}'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))