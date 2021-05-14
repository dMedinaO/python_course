i= 1
while i != 2:
    pd = int(input("\nIngrese el total de la pension en Dolares= "))
    print("\nAmbos estan vacunados contra el COVID 19?")
    print("1. SI")
    print("2. NO\n")
    co = int(input("Selecione el numero dependiendo de su situacion = "))
    print("\nEsta habilitado los viajes internaciones tanto en Chile como en Francia?")
    print("1. SI")
    print("2. NO\n")
    ae = int(input("Selecione el numero dependiendo de su situacion = "))
    print("\n\n")
    pd1 = (pd * 0.1)
    if (co == 1) and (ae == 1):
        if (pd1 >= 7500):
            print("El 10% de su AFP cubre los gastos del viaje, incluyendo los gastos adicionales como en souvenir, comidas en restaurants, entre otros.")
        elif (pd1 < 7500) and (pd1 >= 5000):
            print("El 10% de su AFP cubre los gastos del viaje, pero no los gastos adicionales")
        elif pd1 < 5000:
            print("El 10% de su AFP NO cubre los gatos del viaje.")
    elif (co == 2) and (ae == 2):
        print("Deberia Vacunarse contra el COVID 19 para poder realizar el viaje y \ndeberia esperar que habiliten los viajes internaciones tanto en Chile como en Francia.")
    else:
        if co == 2 and ae == 1:
            print("Deberia Vacunarse contra el COVID 19 para poder realizar el viaje.")
        elif ae == 2 and co == 1:
            print("Deberia esperar que habiliten los viajes internaciones tanto en Chile como en Francia ")
    print("\nDesea seguir con la aplicacion?")
    print("1. SI")
    print("2. NO\n")
    i = int(input("Selecione el numero dependiendo de su situacion = "))
    
    
    
