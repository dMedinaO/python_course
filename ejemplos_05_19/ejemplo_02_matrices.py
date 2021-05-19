mi_matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(mi_matriz)
print(mi_matriz[0])
print(mi_matriz[1])
print(mi_matriz[2])

for i in range(len(mi_matriz)):
	for j in range(len(mi_matriz[i])):
		print("{} {} tiene el valor de {}".format(i,j,mi_matriz[i][j]))

mi_lista_dos = [1, 4]
mi_lista_dos.append(mi_matriz)

print(mi_lista_dos[-1][0][1])