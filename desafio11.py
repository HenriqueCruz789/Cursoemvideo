#DESAFIO 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
a = float(input('Digite a largura da parede em metros:'))
b = float(input('Digite a altura da parede em metros:'))
c = a*b #área total da parede
d = c/2 #área total dividido por 2mts que equivale a 1 litro de tinta
print('A área total da parede é de {} m², e você vai precisar de {} litros de tinta para pintá-la.'.format(c, d))
