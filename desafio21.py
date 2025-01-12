#Faça um programa python que abra e reproduza o áudio de um arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('des21.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
