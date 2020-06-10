from math import radians, sin, cos, tan
ângulo = float(input('Digite um ângulo: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo d e{} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))