# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE
# DIAS PELOS QUAIS O CARRO FOI ALUGADO, CALCULE O PREÇO A PAGAR! SABENDO QUE O CARRO CUSTA R$ 60,00 DIA
# E R$ 0,15 POR KM RODADO.
d = int(input('Quantos dias o carro foi alugado?'))
k = float(input('Quantos Km rodados? '))
r = d * 60
z = k * 0.15
t = r + z
# ou r = (d * 60) + (k * 0.15)
# print(''O total a pagar é de R${:.2f}.'.format(r)')
print('O total a pagar é de R${:.2f}.'.format(t))
