# 7. Ingresar por teclado el nombre y el signo de cualquier persona e imprima, el
# nombre solo si la persona es signo Aries

nombre = input("Ingrese su nombre: ")
signo = input("Ingrese su signo: ").lower()

if signo == "aries": 
    print(f"Hola {nombre}")
else:
    print(f"No es aries")