ppm=int(input("ingrese las PPM registradas en el ambiente:"))
poblacion=int(input("ingrese la cantidad de habitantes en la poblacion:"))

if ppm >= 10:
	print("alerta negra. Notificar a la comunidad")
elif ppm >7 and ppm <10:
	print("alerta roja")
	if poblacion >5000000: 
		print("Notificar a la comunidad")
elif ppm > 4 and ppm <= 7:
	print("alerta naranja")
	if poblacion >7000000:
		print("Notificar a la comunidad")
elif ppm > 2 and ppm <=4: 
	print("alerta amarilla")
else:
	print("no se decreta alerta")

	
	
