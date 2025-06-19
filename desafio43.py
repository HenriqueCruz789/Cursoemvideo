peso = float(input('Qual o seu peso ? (KG):'))
altura = float(input('Qual é a sua altura? (M):'))
#a = peso
#b = pow(altura, 2)
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu imc é {:.1f}!!!'.format(imc))
    print('Você está ABAIXO DO PESO NORMAL!')
elif 18.5 <= imc < 25:
    print('Seu imc é {:.1f}!!!'.format(imc))
    print('Parabéns!!! Você está na faixa de PESO IDEAL!')
elif 25 <= imc  < 30:
    print('Seu imc é {:.1f}!!!'.format(imc))
    print('Você está em SOBREPESO')
elif 30 <= imc  < 40:
    print('Seu imc é {:.1f}!!!'.format(imc))
    print('Cuidado você está em OBESIDADE')
else:
    print('Seu imc é {:.1f}!!!'.format(imc))
    print('Perigo!!! Você está em OBESIDADE MÓRBIDA')

