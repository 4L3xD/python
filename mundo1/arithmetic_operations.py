# ** ou pow(2,3) == exponenciação
# // divisão inteira
# / divisão real
# % resto da divisão
# **(1/2) raiz quadrada
# **(1/3) raiz cubica

print('='*30)
nome = input('Qual é o seu nome? ')
#Alinhamento a esquerda
print('Prazer em te conhecer {:<20}!'.format(nome))
#Alinhamento a direita
print('Prazer em te conhecer {:>20}!'.format(nome))
#Centralizado
print('Prazer em te conhecer {:^20}!'.format(nome))
#Com caracter
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
# numero de casas decimais
print('A divisão vale {:.3f}'.format(n1/n2), end=' ')
print('A potência vale {:.3f}'.format(n1**n2))