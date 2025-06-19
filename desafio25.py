#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA
#E DIGA SE ELA TEM 'SILVA' NO NOME
#---------------------------------------------------------------------

name = str(input('Qual é o seu nome completo? ')).strip()
print('O Seu nome tem Silva? {}'.format('silva' in name.lower()))



