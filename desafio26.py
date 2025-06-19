#FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO
#E MOSTRE:
#- QUANTAS VEZES APARECE A LETRA 'A'
#- EM QUE POSIÇÃO APARECE PELA PRIMEIRA VEZ
#- EM QUE POSIÇÃO APARECE PELA ÚLTIMA VEZ
#------------------------------------------------------------
f_1 = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} na frase.'.format(f_1.count('A')))
print('A primeira letra A, apareceu na posição {}'.format(f_1.find('A')+1))
print('A última letra A apareceu na posição {}'.format(f_1.rfind('A')+1))

