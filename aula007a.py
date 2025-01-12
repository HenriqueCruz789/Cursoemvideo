n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma entre {} e {} é = {} ,\n a multiplicação é = {},\n a divisão é = {:.2f},\n'.format(n1, n2, s, m, d), end=' ')
print('A divisão inteira entre {} e {} é = {},\n e a potencialização é = {}'.format(n1, n2, di, e))



