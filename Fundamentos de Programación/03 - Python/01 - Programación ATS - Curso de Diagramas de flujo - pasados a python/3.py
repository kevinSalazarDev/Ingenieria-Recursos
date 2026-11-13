# 3. Sacar la hipotenusa de un triángulo rectángulo, pidiendo al usuario
# el valor de los 2 catetos

from math import sqrt


cateto_opuesto = float(input("Ingrese el cateto opuesto: "))
cateto_adyacente = float(input("Ingrese el cateto adyacente: "))

hipotenusa = sqrt((cateto_opuesto)**2 + (cateto_adyacente)**2)

print(hipotenusa)


