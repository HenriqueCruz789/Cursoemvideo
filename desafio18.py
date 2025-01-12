#FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DE
# SENO, COSSENO E TANGENTE DESSE ANGULO
'''import math
angulo = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(angulo))
print('O ângulo de {}, tem o seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {}, tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {}, tem a tangente de {:.2f}'.format(angulo, tangente))'''
# ou o programa pode ser realizado na forma de baixo:
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(angulo))
print('O ângulo de {}, tem o seno de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {}, tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {}, tem a tangente de {:.2f}'.format(angulo, tangente))



