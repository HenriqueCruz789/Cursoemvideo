#UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO.
#FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME ESCOLHIDO
'''import random
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))'''
# ou pode ser escrito da forma a seguir
from random import choice
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
