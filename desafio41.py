from datetime import date
year = int(input("Que ano que você nasceu?"))
referencia = date.today().year
resultado = referencia - year
if resultado <= 9:
    print('Você é da categoria - Mirim')
    print("Pois você tem {} anos".format(resultado))
elif resultado <= 14:
    print('Você é da categoria - Infantil')
    print("Pois você tem {} anos".format(resultado))
elif resultado <=19:
    print('Você é da categoria - Junior')
    print("Pois você tem {} anos".format(resultado))
elif resultado ==20:
    print('Você é da categoria - Sênior')
    print("Pois você tem {} anos".format(resultado))
else:
    print('Você é da categoria - Master')
    print('Pois você tem {} anos'.format(resultado))

