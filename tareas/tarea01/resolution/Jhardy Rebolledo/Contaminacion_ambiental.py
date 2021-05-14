#Contaminacion Ambiental en Región Metropolitana
#La entrada son PPM y Poblacion. / La Salida es el tipo de alerta y si se notifica a la comunidad o no.
PPM = int(input("Estado de contaminacion(PPM):"))
Poblacion = int(input("Poblacion(M):"))
if PPM >= 10:
	print("Alerta Negra")
else:
	if PPM > 7 and PPM < 10:
		print("Alerta roja")
		if Poblacion > 5:
			print("Se notifica Alerta roja a la comunidad")
	else:
		if PPM > 4 and PPM <= 7:
			print("Alerta naranja")
			if Poblacion > 7:
				print("Se notifica Alerta naranja a la comunidad")
		else:
			if PPM > 2 and PPM <= 4:
				print("Alerta amarilla")
			else:
				if PPM <= 2:
					print("No se declara alerta")		
