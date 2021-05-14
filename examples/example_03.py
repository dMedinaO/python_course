#ejemplo de recibir variables por entrada estandar

nombre_cadete = input("Ingresa el nombre del cadete: ")
nota_01 = float(input("Ingrese nota 1 "))
nota_02 = float(input("Ingrese nota 2 "))
nota_03 = float(input("Ingrese nota 3 "))
nota_04 = float(input("Ingrese nota 4 "))
nota_05 = float(input("Ingrese nota 5 "))

minimo_aprob = float(input("Ingrese el minimo aprobacion "))

promedio = (nota_01+nota_02+nota_03+nota_04+nota_05)/5

print("Cadete: {} obtuvo una nota de {}".format(nombre_cadete, promedio))

#sentencias de condiciones
if promedio >= minimo_aprob:
	print("Cadete Aprobado")
else:
	print("Cadete No Aprobado")