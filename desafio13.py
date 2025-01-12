#DESAFIO 13: Faça um algoritmo que leia um salário de um funcionário e mostre o seu novo salário,
# com 15% de aumento.
a = float(input('Digite o valor do salário do funcionário: R$'))
b = a * (15/100)
c = a + b
print(' O salário que era de R$ {:.2f}, com o aumento de 15%, agora será de R${:.2f}. '.format(a, c))