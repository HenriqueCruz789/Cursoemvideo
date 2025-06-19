n1 = int(input('Digite um número inteiro:'))
n2 = int(input('Digite mais um número inteiro:'))
if n1 > n2:
    print('O primeiro valor é maior!')
    print('O número {} é maior que {}.'.format(n1, n2))
elif n2 > n1 :
    print('O segundo valor é maior!')
    print('O número {} é maior que {}.'.format(n2, n1))
else:
    print('Não existe valor maior, os dois são iguais!')
    print('O número {} é igual a {}!'.format(n1, n2))

