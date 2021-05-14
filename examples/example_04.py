#definir mi propia funcion promedio
def estimar_promedio(notas):

	#promedio = (notas[0]+notas[1]+nota[2]+nota[3]+nota[4])/5
	promedio = 0

	for i in range(len(notas)):
		promedio = promedio + notas[i]
	promedio = promedio/len(notas)
	
	return promedio

def revisar_aprobacion(promedio, minimo_aprob):

	response = "REPROBADO"
	if promedio >= minimo_aprob:
		response="APROBADO"

	return response

numero_cadetes = int(input("Ingrese el numero de cadetes a procesar "))

if numero_cadetes <=0:
	print("Debes ingresar un numero correcto")
else:
	
	min_aprobacion = float(input("Ingrese el minimo de aprobacion "))
	lista_archivo = []

	for i in range(numero_cadetes):
		nombre_cadete = input("Ingresa el nombre del cadete: ")
		nota_01 = float(input("Ingrese nota 1 "))
		nota_02 = float(input("Ingrese nota 2 "))
		nota_03 = float(input("Ingrese nota 3 "))
		nota_04 = float(input("Ingrese nota 4 "))
		nota_05 = float(input("Ingrese nota 5 "))

		notas = [nota_01, nota_02, nota_03, nota_04, nota_05]
		promedio_cadete = estimar_promedio(notas)
		print("Promedio de notas cadete {} es {}".format(nombre_cadete, promedio_cadete))
		response_aprob = revisar_aprobacion(promedio_cadete, min_aprobacion)

		linea_file = "{},{},{},{},{},{},{},{}".format(nombre_cadete, nota_01, nota_02, nota_03, nota_04, nota_05, promedio_cadete, response_aprob)
		lista_archivo.append(linea_file)
	
	print("Export file")

	file_export = open("mi_archivo_demo.csv", 'w')

	for line in lista_archivo:
		file_export.write(line+"\n")
	file_export.close()




