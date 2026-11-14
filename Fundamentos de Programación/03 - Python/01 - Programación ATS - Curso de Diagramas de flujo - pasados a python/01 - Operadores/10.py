'''
10. Un alumno desea saber cuál será su calificación final en la materia de
Algoritmos. Dicha calificación se compone de los siguientes porcentajes:

• 55% del promedio de sus tres calificaciones parciales.
• 30% de la calificación del examen final.
• 15% de la calificación de un trabajo final. (Propuesto)

'''

from errno import EDEADLK


parcial1 = float(input("Ingrese la nota del primer parcial: "))
parcial2 = float(input("Ingrese la nota del segundo parcial: "))
parcial3 = float(input("Ingrese la nota del tercer parcial: "))
promedio_parcial = (parcial1+parcial2+parcial3)/(3)
promedio_parcial = promedio_parcial*55/100

examen_final = float((input("Ingrese la nota del examen final: ")))
examen_final = examen_final*30/100

trabajo_final = float(input("Ingrese la nota del trabajo final: "))
trabajo_final = trabajo_final*15/100

nota_final = promedio_parcial+examen_final+trabajo_final
print(nota_final)

