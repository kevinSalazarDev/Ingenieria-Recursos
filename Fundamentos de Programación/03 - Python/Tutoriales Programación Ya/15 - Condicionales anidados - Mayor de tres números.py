numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el terecer número: "))

if numero1 > numero2:
    if numero1 > numero3:
        print("El número mayor es", numero1)
    else:
        print("El número mayor es:", numero3) 

else: 
    if numero2 > numero3:
        print("El número mayor es", numero2)
    else:
        print("El número mayor es", numero3)
