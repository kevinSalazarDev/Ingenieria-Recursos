# 1. Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara
# si su promedio de tres calificaciones es mayor o igual a 10.5; reprueba en caso
# contrario.

nota1 = float(input("Ingrese la primer nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercer nota: "))

promedio = (nota1+nota2+nota3)/(3)

if promedio >= 7:
    print("Aprobado")
else:
    print("Reprobado")