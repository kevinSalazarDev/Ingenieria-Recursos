# Hacer un programa para ingresar el radio de un círculo
# y se reporte su área y la longitud de la circunferencua
# área = pi * r**2
# longitud = 2 * pi * r

from math import pi


radio = float(input("Ingrese el radio de un círculo: "))

area = pi * radio**2
longitud = 2 * pi * radio

print(f"El áreas es:{area:.2f}")
print(f"La longitud es:{longitud:.2f}")


