# Hacer un programa que pida 3 números y determine cuál es el 
# mayor

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

if numero1 == numero2 == numero3:
    print("Los tres son iguales")

elif numero1 >= numero2 and numero1 >= numero3:
    print(f"{numero1} es mayor")

elif numero2 >= numero1 and numero2 >= numero3:
    print(f"{numero2} es mayor")

elif numero3 > numero1 and numero3 > numero2:
    print(f"{numero3} es mayor") 

    


