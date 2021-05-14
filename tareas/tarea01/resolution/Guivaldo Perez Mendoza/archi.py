ppm = float(input("Ingrese ppm:"))

print("Su ppm es",ppm)

if ppm >= 10:
    print("La zona se encuentra en alerta roja")
    print("Se notifica a la comunidad")


if ppm > 7 and ppm < 10:
    print("Se declara alerta roja")
    print("si la poblacion es > 5000000 se notifica a la comunidad")

if ppm > 4 and ppm <= 7:
    print("Alerta naranja")
    print("si la poblacion es > 7000000 se notifica a la comunidad")


elif ppm > 2 and ppm <= 4:
    print("Alerta amarilla") 
elif ppm <= 2:
    print("No se declara alerta")