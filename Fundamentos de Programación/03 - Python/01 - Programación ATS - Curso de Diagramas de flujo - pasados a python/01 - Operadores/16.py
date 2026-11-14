# 16. Volumen y Área de una Esfera. (Propuesto)

from math import pi


radio = float(input("Ingrese el radio de la esfera: "))

volumen = (4/3)*(pi)*(radio)**3
area = (4)*(pi)*(radio)**2

print(f"El volumen es: {volumen}")
print(f"El área es: {area}")