#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE
#E DIGA SE ELA COMEÇA OU NÃO COM O NOME 'SANTO'
#-------------------------------------------------------
cidade = str(input('Digite o nome da sua cidade:')).strip()
print(cidade[:5].upper() == 'SANTO')


