# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de um trabalho dos alunos.
#Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada

from random import shuffle
n1 = str(input('Digite o nome do primeiro aluno:'))
n2 = str(input('Digite o nome do segundo aluno:'))
n3 = str(input('Digite o nome do terceiro aluno:'))
n4 = str(input('Digite o nome do quarto aluno:'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)
