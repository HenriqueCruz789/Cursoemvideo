#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999
#E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADOS:
#EXEMPLO:
#DIGITE UM NÚMERO: 1834
#UNIDADE: 4
#DEZENA: 3
#CENTENA: 8
#MILHAR: 1
#--------------------------------------------------------------------------------------

numero = int(input('Digite um número:  '))
u = numero // 1 % 10
d = numero // 10 % 10
cent = numero // 100 % 10
milhar = numero // 1000 % 10
print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(cent))
print('Milhar: {}'.format(milhar))
