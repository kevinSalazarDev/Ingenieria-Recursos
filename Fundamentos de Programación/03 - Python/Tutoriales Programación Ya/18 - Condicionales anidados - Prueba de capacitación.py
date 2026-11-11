total_preguntas = int(input("Ingrese el total de preguntas que se realizaron: "))
preguntas_correctas = int(input("Ingrese las preguntas que contestó correctamente: "))

if total_preguntas <= 0:
    print("Error: el total de preguntas debe ser mayor que 0.")
elif preguntas_correctas < 0 or preguntas_correctas > total_preguntas:
    print("Error: las respuestas correctas deben estar entre 0 y el total de preguntas.")
else:
    porcentaje = preguntas_correctas * 100 / total_preguntas

    if porcentaje >= 90:
        print("Nivel máximo")
    elif porcentaje >= 75:
        print("Nivel medio")
    elif porcentaje >= 50:
        print("Nivel regular")
    else:
        print("Fuera de nivel")
