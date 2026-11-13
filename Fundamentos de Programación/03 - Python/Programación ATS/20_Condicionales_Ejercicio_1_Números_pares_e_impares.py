# Hacer un programa que pida 2 números y de cuenta cúal de
# ellos es par, o si ambos los son

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

if numero1 % 2 == 0 and numero2 % 2 == 0: 
    print("Ambos son par")

elif numero1 % 2 == 0:
    print(f"{numero1} es par")

elif numero2 % 2 == 0:
    print(f"{numero2} es par")
    
else:
    print("Ninguno es par")



