''' 6. Un obrero necesita calcular su salario semanal, el cual se obtiene de la
siguiente manera:
• Si trabaja 40 horas o menos se le paga $16 por hora
• Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas
y $20 por cada hora extra. (Propuesto)
'''

horas_semanales =  float(input("Ingrese las horas de trabajo semanal: "))

if horas_semanales <= 40:
    salario_semanal = horas_semanales*16

else:
    horas_extras = horas_semanales-40
    hora = horas_semanales - horas_extras
    salario = (hora*16)+(horas_extras*20)     

print(f"El salario es: ${salario}")