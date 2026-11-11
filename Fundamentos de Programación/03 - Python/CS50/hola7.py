# Pedir el nombre completo, quitar espacios exteriores y capitalizar cada palabra.
nombre_completo = input("¿Cuál es tu nombre? ").strip().title()

# Separar el nombre y el apellido sin fallar si el usuario escribe un solo nombre.
partes = nombre_completo.split(maxsplit=1)
nombre = partes[0] if partes else ""
apellido = partes[1] if len(partes) > 1 else ""

# Saludar usando el nombre.
if nombre:
    print(f"Hola, {nombre}")
else:
    print("Hola")
