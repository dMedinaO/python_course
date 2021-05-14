'''
Las condiciones o decisiones son segmentos de codigo que se ejecutan dependiendo de un 
valor o una condicion que nosotros declaremos. Al igual que en la vida, las condiciones permiten ejecutar
codigo, si queremos darnos un lujo, comprar un regalo a su novia, salir a vacacionar, etc.

Para trabajar con condiciones en python existen las palabras reservadas: if, else y elif, un segmento clasico de
codigo de condiciones es como sigue

if condiciones:
	acciones -> importante siempre se debe tabular para definir el bloque de codigo que se quiere ejecutar
else:#significa en caso contrario
	acciones alternativas

'''

#ejemplo de evaluacion de notas
nota_1 = int(input("Ingresa tu nota"))

if nota_1 > 4:
	print("Alumno aprobado")
else:
	print("Alumno reprobado")


#tambien podemos comparar palabras
nombre = input("Ingrese un nombre")

if nombre == "Juan":
	print("El nombre ingresado coincide")
else:
	print("No es Juan")





