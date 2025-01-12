#DESAFIO 10: Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#		Considere o dólar à R$ 3,27
a = float(input('Digite o valor que você possui na carteira? R$'))
print('Com o valor de R${:.2f}, você consegue comprar US${:.2f}.'.format(a, a/3.27))
