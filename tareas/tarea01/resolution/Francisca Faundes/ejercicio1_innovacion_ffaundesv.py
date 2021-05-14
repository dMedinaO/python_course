
sueldo_pedro= float(input("ingrese la cantidad de dinero que posee Pedro en su AFP en dolares:"))

total_retiro=(sueldo_pedro/10) 

print("el monto total que Pedro puede retirar en dolares es:",total_retiro)

if total_retiro >= 7500:

	vacuna=input("indique si Pedro y su pareja están vacunados con si o no: ")
	habilitacion=input("indique si los aeropuertos están habilitados con si o no:")

	if vacuna == "si" and habilitacion=="si":
		print("felicidades! Pedro puede realizar el tour con su novia")
	else:
		print("Pedro no puede realizar el viaje ya que no se cumple uno de los requisitos")
else:
	print("Pedro no puede realizar el tour debido a que no posee el dinero suficiente para costear el viaje y los gastos adicionales")	


	
