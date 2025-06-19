from datetime import date
ano = int(input('Que ano você nasceu?'))
print
referencia = date.today().year
idade = ano - referencia
resultado = - idade
vazio = resultado - 18
alistamento = referencia - vazio
if resultado < 18:
    print('Ainda não é hora de se alistar para o exército!')
    print('Você tem {} anos e ainda falta(m) {} ano(s) para se alistar.'.format(resultado, - vazio))
    print('Seu alistamento será em {}'.format(alistamento))
elif resultado == 18:
    print('Você precisa se alistar ao exército!!!')
    print('Você tem {} anos.'.format(resultado))
    print('Seu alistamento será em {}'.format(alistamento))
else:
        print('Já passou a horar de você se alistar ao exército!!!')
        print('Você tem {} anos e passaram-se {} anos do período correto de alistamento! '.format(resultado, vazio))
        print('Seu alistamento era em {}'.format(alistamento))




#print('A idade é {}'.format(resultado))
