print("valor PPM")
PPM_valor = input()
print("Poblacion")
Poblacion = input()
PPM_valor = int(PPM_valor)
Poblacion = int(Poblacion)
if (PPM_valor>= 10):
    print("alerta negra y se requiere notificar a la comunidad")
if (PPM_valor >=7 and PPM_valor < 10):
    if(Poblacion>5000000):
        print("alerta roja y se requiere notificar a la comunidad")
    else:
        print("alerta roja sin notificar a la comunidad")
if (PPM_valor>4 and PPM_valor <=7):
    if(Poblacion>7000000):
        print("alerta naranja y se le requiere notificar comunidad")
    else:
        print("alerta naranja y no se le requiere notificar a la comunidad")
if (PPM_valor>=2 and PPM_valor<4):
    print("alerta amarilla y no se requiere notificara la comunidad")
if (PPM_valor<2):
    print("sin alerta")