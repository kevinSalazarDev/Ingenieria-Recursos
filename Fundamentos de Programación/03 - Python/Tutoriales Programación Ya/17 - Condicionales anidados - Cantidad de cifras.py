num = int(input("Ingrese un número positivo de hasta tres cifras: "))

if num < 10:
    print("El número tiene 1 cifra")
else: 
    if num < 100:
        print("El número tiene 2 cifras")
    else:
        if num < 1000:
            print("El número tiene 3 cifras")
        else:
            print("Error el número de cifras es mayor")
