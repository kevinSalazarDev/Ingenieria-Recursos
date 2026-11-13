'''
Contruir un programa que simule el funcionamiento de una 
calculadora que puede realizar las cuatro operaciones aritméticas
básicas (suma, resta, multiplicación y división). El usuario debe
especificar la operación con el primer caracter del nombre de la
operación.

S, s - Suma
R, r - Resta
P, p, M, m - Multipicación
D, d - División

'''

num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))
print(f"Ingrese una de las siguientes opciones:\nS, s - Suma\nR, r - Resta\nP, p, M, m - Multipicación\nD, d - División")

caracter = input("Ingrese el primer caracter del nombre de la operación: ")

if caracter == "s" or caracter == "S":
    suma = num1 + num2
    print(suma)

elif caracter == "r" or caracter == "R":
    resta = num1 - num2
    print(resta)

elif caracter == "p" or caracter == "P" or caracter == "M" or caracter == "m":
    multiplicacion = num1 * num2
    print(multiplicacion)

elif caracter == "d" or caracter == "D":
    division = num1 / num2
    print(division)

else:
    print("No es el caracter correcto")