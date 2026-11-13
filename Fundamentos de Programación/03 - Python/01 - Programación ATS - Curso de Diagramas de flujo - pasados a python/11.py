# 11. Calcular la cantidad de segundos que están incluidos en el número de horas,
# minutos y segundos ingresados por el usuario.

horas = float(input("Ingrese las horas: "))
minutos = float(input("Ingrese los minutos: "))
segundos = float(input("Ingrese los segundos: "))

horas_a_segundos = horas*3600
minutos_a_segundos = minutos*60
segundos_a_segundos = segundos*1

total_segundos = horas_a_segundos+minutos_a_segundos+segundos_a_segundos
print(total_segundos)
