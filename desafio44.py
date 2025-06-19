print('{:=^40}' .format('LOJA DO RICK' ))
preco = float(input('Qual é o valor das compras? R$'))
print('''Qual a forma de pagamento:
[1] - À vista (dinheiro/cheque)
[2] - À vista (Cartão/débito)
[3] - Crédito (2x-Cartão)
[4] - Crédito (3x/ou mais - Cartão)''')
opcao = int(input('Qual a forma de pagamento? (1,2,3,4):'))
a = preco * (10/100)
b = preco - a
d = preco * (5/100)
debito = preco - d
juros = preco * (20/100)
j = preco + juros
if opcao == 1 :
        print('O valor total da compra é R${}, e você pagará R${:.2f}'.format(preco, b))
        print('Você terá 10 % de desconto!!!')
if opcao == 2 :
        print('O valor a pagar será R${:.2f}'.format(debito))
        print('Você terá 5 % de desconto!!!')
if opcao == 3 :
        print('O valor a pagar será R${:.2f}'.format(preco))
        print('Você pagará o valor total sem juros!!!')
if opcao == 4 :
        print('O valor a pagar será R${:.2f}'.format(j))
        print('Você pagará o valor total com um acréscimo de 20%, referente aos juros!!!')
#melhorar conforme video