velocidade = float(input('Qual a velocidade do carro?'))
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Multado!Você excedeu o limite de velocidade que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format((velocidade-80)*7))
    print('Tenha um bom dia! Dirija com segurança')