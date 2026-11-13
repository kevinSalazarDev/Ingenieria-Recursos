# Hacer un programa que pida un caracter e indique si es una
# vocal o no.
 
caracter = input("Ingrese un caracter: ").lower()

if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":  
    print(f"{caracter} es una vocal")

else:
    print(f"{caracter} no es una vocal")
