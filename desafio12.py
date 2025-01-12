#DESAFIO 12: Faça um algoritmo que leia o preço de um produto
# e mostre o seu novo preço, com 5% de desconto.
a = float(input('Digite o valor do produto? R$'))
b = a * (5/100)
c = a - b
print(' O valor do produto que era R${:.2f}, com o desconto de 5%, agora será de R${:.2f}'.format(a, c))