'''
A estas alturas hemos visto lo basico de un curso de python1, en este ejemplo, trabajaremos 
con lectura y escritura de archivos de texto. Para ello, tomaremos un archivo, leeremos los
nombres existentes en el y obtendremos las iniciales de ellos, armando un diccionario el cual
se exportara a un archivo de salida
'''

file_open = open('archivo_input.txt', 'r')#la r significa lectura, la w escritura, entre las principales

#la informacion del archivo la guardaremos en una lista
diccionario_iniciales = {}

line = file_open.readline()#leemos la primera linea para formar el ciclo

while line:#no sabemos cuantas lineas son, leemos hasta que se acabe el archivo

	line = line.replace("\n", "")#le quitamos el enter a la linea

	names = line.split(" ")#con spline seperamos por espacio
	iniciales = "{}{}".format(names[0][0], names[1][0])
	
	#agregamos la key generada al diccionario
	diccionario_iniciales.update({iniciales:line})
	
	line = file_open.readline()#continuamos leyendo

file_open.close()#siempre debemos cerrar el archivo abierto

#exportamos a un archivo
file_export = open("archivo_iniciales.txt", 'w')#declaramos el archivo de salida

for inicial in diccionario_iniciales:

	line_print = "{}:{}\n".format(inicial, diccionario_iniciales[inicial])#el \n representa un enter o salto de lineas
	file_export.write(line_print)

file_export.close()

