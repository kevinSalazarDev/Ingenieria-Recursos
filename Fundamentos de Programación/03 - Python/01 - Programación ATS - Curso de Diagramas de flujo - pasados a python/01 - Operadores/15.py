'''
15. Tres personas deciden invertir su dinero para fundar un empresa. Cada una de
ellas invierte una cantidad distinta. Obtener el porcentaje que cada quien invierte
con respecto a la cantidad total invertida.
'''

from tkinter import N


inversionista1 = float((input("Ingrese la inversión del primer inversionista: ")))
inversionista2 = float((input("Ingrese la inversión del segundo inversionista: ")))
inversionista3 = float((input("Ingrese la inversión del tercer inversionista: ")))

inversion_total = inversionista1+inversionista2+inversionista3

porcentaje1 = (inversionista1*100)/(inversion_total)
porcentaje2 = (inversionista2*100)/(inversion_total)
porcentaje3 = (inversionista3*100)/(inversion_total)

print(f"El porcentaje del primer inversionista es: {porcentaje1}%")
print(f"El porcentaje del segundo inversionista es: {porcentaje2}%")
print(f"El porcentaje del tercer inversionista es: {porcentaje3}%")