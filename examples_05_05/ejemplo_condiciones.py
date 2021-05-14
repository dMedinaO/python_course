#determinar si enviamos una alerta de sismo
#la alerta de sismo se enviara si y solo si, el valor de la actividad es mayor a 5
#num_habitantes > 1 -> si envio la alerta

valor_escala = float(input("Favor ingrese el valor en escala "))
num_habitantes = float(input("Favor ingrese el numero de habitantes en MM ")) 

'''
#opcion A
print("Valor escala {}".format(valor_escala))
if valor_escala > 5:

	print("Si hay un sismo")

	if num_habitantes > 1:
		print("Enviar alerta")
	else:
		print("No enviar alerta")

else:
	print("No hay un sismo")


#opcion B
if valor_escala > 5 and num_habitantes >1:
	print("Si hay un sismo y debo enviar alerta")

else:
	if valor_escala > 5 and num_habitantes <=1:
		print("Si hay un sismo")

	else:
		print("No hay un sismo")

'''
#opcion C
if valor_escala > 5 and num_habitantes >1:
	print("Si hay un sismo y debo enviar alerta")

elif valor_escala > 5 and num_habitantes <=1:
	print("Si hay un sismo")
else:
	print("No hay un sismo")
