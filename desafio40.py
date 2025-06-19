n1 = float(input('Qual a primeira nota?'))
n2 = float(input('Qual a segunda nota?'))
media = (n1 + n2)/2
if media < 5.0:
    print('Reprovado!!!')
    print('A média final foi {:.1f}'.format(media))
elif 7 > media >= 5.0:
    print('Recuperação!!!')
    print('A média foi {:.1f} e precisava ser 7.0 para ser aprovado!'.format(media))

else:
    print('Aprovado!!!')
    print('Parabéns a sua média foi {}'.format(media))
