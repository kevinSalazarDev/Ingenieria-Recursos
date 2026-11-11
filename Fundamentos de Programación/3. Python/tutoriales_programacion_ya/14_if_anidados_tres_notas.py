nota_1 = int(input("Ingrese la primera nota: "))
nota_2 = int(input("Ingrese la segunda nota: "))
nota_3 = int(input("Ingrese la tercera nota: "))

promedio = (nota_1+nota_2+nota_3)/3

if promedio >=7:
    print("Aprobado")
else:
    if promedio >=4:
        print("Regular")
    else:
        print("Reprobado")