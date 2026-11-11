total_preguntas = int(input("Ingrese el total de preguntas que se realizaron: "))
preguntas_correctas = int(input("Ingrese las preguntas que contestó correctamente: "))

porcentaje = preguntas_correctas * 100 / total_preguntas

if porcentaje >= 90:
    print("Nivel máximo")
else:
    if porcentaje >= 75:
        print("Nivel medio")
    else:
        if porcentaje >= 50:
            print("Nivel regular")
        else:
            print("Fuera de nivel")
        
