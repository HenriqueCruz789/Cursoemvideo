v = float(input('Qual é o valor da casa? R$'))
s = float(input('Qual é o seu salário? R$'))
y = int(input('Em quantos anos você pretende pagar?'))
meses = y * 12
parcelas = v / meses
salario = s * (30/100)
porcentagem = parcelas * 100 / s
if parcelas <= salario:
    print('Emprestimo aprovado! As parcelas serão menores ou iguais a 30% do seu salário')
    print('As parcelas serão de R$ {:.2f}'.format(parcelas))
else:
    print('Não foi possível realizar o empréstimo! Devido a parcela ser maior que 30% do seu salário')
    print('Valor das parcelas seriam de R$ {:.2f}'.format(parcelas))
    print('Ou seja, {:.2f} % do seu salário!'.format(porcentagem))











