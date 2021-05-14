'''
Este ejemplo representa como declarar y trabajar con las variables,
ademas permite mostrar las diferentes formas de imprimir por pantalla.
Nota:
#con el simbolo # se pueden comentar lineas
'''

#declararemos diferentes tipos de variables
variable_int = 5
variable_float = 5.3
variable_char = 'c'
variable_string = "nombre"

#podemos imprimir las variables usando la funcion print()
print("Imprimir variables")#print recibe un texto o una variable o conjunto de variables formateadas
print(variable_int)
print(variable_float)
print(variable_char)
print(variable_string)

#podemos forzar a las variables a ser de un determinado tipo
variable_cast_int = int(5.3)
variable_cast_float = float(5)

#incluso los string se pueden castear cuando tienen sentido
variable_cast_string = float("5.432")

print("Variables casteadas")
print(variable_cast_int)
print(variable_cast_float)
print(variable_cast_string)

#finalmente podemos formatear los string para imprimirlos como una cadena con sentido de oracion
variable_imprimir = "Queremos formar una frase con {} oraciones que contenga la palabra {} y que en promedio se use {} veces".format(variable_int, variable_string, variable_float)
print(variable_imprimir)

#se puede hacer lo mismo, simplemente dentro del print
print("Queremos formar una frase con {} oraciones que contenga la palabra {} y que en promedio se use {} veces".format(variable_int, variable_string, variable_float))



