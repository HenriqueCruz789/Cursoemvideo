#FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA
#MOSTRANDO EM SEGUIDA O PRIMEIRO E O ULTIMO NOME SEPARADAMENTE.
#EX.: ANA MARIA DE SOUZA
#PRIMEIRO: ANA
#ÚLTIMO : SOUZA
#----------------------------------------------------------------------
nome_1 = str(input('Digite o seu nome:')).strip().upper()
print('Prazer em te conhecer!!!')
print('O seu primeiro nome é: {}'.format(nome_1.split()[0]))
print('O seu último nome é: {}'.format(nome_1.split()[-1]))

#Vc pode criar com mais uma variável, conforme resolução do Guanabara
#n = str(input('Digite o seu nome: ')).strip()
#nome = n.split()
#print('Muito prazer em conhecer!!!')
#print('Seu primeiro nome é {}'.format(nome[0]))
#print('Seu último nome é {}'.format(nome[len(nome)-1]))
