# Escreva um programa que converta uma temperatura digitada em °C e converta para °F
T = float(input('Digite a temperatura atual em °C:'))
F = (T * 1.8) + 32
# ou F = ((9 * T) / 5) + 32
print('A temperatura de {} °C corresponde a {} °F!'.format(T, F))
