#DESAFIO 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
a = float(input('Digite o valor em metros:'))
print('O valor {:.2f} mts, convertidos para cm é = {:.0f} e convertido em mm é = {:.0f}'.format(a, a*100, a*1000))
#print('A medida de {}m corresponde à:\n{} Km,\n{} hm,\n{} dam,\n{} dm,\n{} cm,\n{} mm'.format(a, (a/1000), (a/100),(a/10),(a*10),(a*100),(a*1000)))
