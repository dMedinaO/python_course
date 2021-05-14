#Evaluando Retirar el 10%
#La entrada son los aeropuertos abiertos, el dinero disponible y si estan vacunados. / La salida si Pedro lograra hacer su viaje.

aeropuertos_abiertos = input("Aeropuertos abiertos, si para confirmar y no para denegar:")

if aeropuertos_abiertos == "si":
	print("Aeropuertos abiertos")
	dinero = int(input("dinero disponible:"))

	if dinero > 7500:
		print("Ha Pedro le alcanza para cubrir el gasto de pasajes y los gastos extras")
		
		Pedro_y_su_novia_estan_vacunados= input("Estan vacunados, si para confirmar y no para denegar:")
		if Pedro_y_su_novia_estan_vacunados == "si":
			print("Pueden viajar, las condiciones se cumplen")
		else:
			if Pedro_y_su_novia_estan_vacunados == "no":
				print("No pueden viajar, no cumplen las condiciones")
	else:
		print("Ha Pedro no le alcanza para cubrir el gasto de pasajes y los gastos extras")
else:
	if aeropuertos_abiertos == "no":
		print("Aeropuertos cerrados")
	else:
		print("Solo se admiten respuesta si o no")
