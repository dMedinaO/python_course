pob = float(input("Ingrese la cantidad de habitantes en Santiago en Millones\n(ejemplo si tiene 8 millones de habitante ingrese '8') --> "))
ppm = int(input("\nIngrese el PPM que se encuentra actualmente Santiago --> "))
if ppm >= 10:
    print("/\/\/\/\/\/\/\ \nAlerta Negra >\n\/\/\/\/\/\/\/")
    print("Se Notifica a la Comunidad")
elif ppm > 7 and ppm < 10:
    print("/\/\/\/\/\/\/\ \nAlerta Roja >\n\/\/\/\/\/\/\/")
    if pob > 5:
        print("Se Notifica a la Comunidad")
elif ppm > 4 and ppm <= 7:
    print("/\/\/\/\/\/\/\ \nAlerta Naranja >\n\/\/\/\/\/\/\/")
    if pob > 7:
        print("Se Notifica a la Comunidad")
elif ppm <= 2:
    print("No se declara alerta")
input("\n\nPresione cualquier tecla para continuar")
    



