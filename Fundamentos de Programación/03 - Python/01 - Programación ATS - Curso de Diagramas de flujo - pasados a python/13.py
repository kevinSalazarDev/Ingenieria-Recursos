# 13. Un maestro desea saber que porcentaje de hombres y que porcentaje de
# mujeres hay en un grupo de estudiantes.

hombres = int(input("Ingrese el número de hombres: "))
mujeres = int(input("Ingrese el número de mujeres: "))

total_alumnos = hombres+mujeres

total_hombres = (hombres*100)/(total_alumnos)
total_mujeres = (mujeres*100)/(total_alumnos)

print(f"Porcentaje de hombres es {total_hombres}% y el porcentaje de mujeres es {total_mujeres}%")
