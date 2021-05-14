nombre_cadete = "Cadete 01"

nota_01 = 4
nota_02 = 5
nota_03 = 2
nota_04 = 6
nota_05 = 7

promedio = (nota_01+nota_02+nota_03+nota_04+nota_05)/5

print("Cadete: {} obtuvo una nota de {}".format(nombre_cadete, promedio))

minimo_aprob = 4.5

#sentencias de condiciones
if promedio >= minimo_aprob:
	print("Cadete Aprobado")
else:
	print("Cadete No Aprobado")
