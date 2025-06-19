from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] - PEDRA
[1] - PAPEL 
[2] - TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
if jogador not in [0, 1, 2]:
    print('Jogada Inválida!!!')
    exit()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('O Computador jogou : {}'.format(itens[computador]))
print('O Jogador jogou: {}'.format(itens[jogador]))
print('-='*11)
if computador == 0: # O COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE!!!')
    elif jogador == 1:
        print('JOGADOR VENCEU!!!')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU!!!')
    else:
        print('Jogada Inválida!!!')
elif computador == 1: # O COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('O COMPUTADOR VENCEU!!!')
    elif jogador == 1:
        print('EMPATE!!!')
    elif jogador == 2:
        print('JOGADOR VENCEU!!!')
    else:
        print('Jogada Inválida!!!')
elif computador == 2: # O COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU!!!')
    elif jogador == 2:
        print('EMPATE!!!')
    else:
        print('Jogada Inválida!!!')