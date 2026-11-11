# preguntar al usuario su nombre, eliminar los espacios en blanco de los dos lados y colocar en mayus la primera letra
nombre = input("¿Cuál es tu nombre? ").strip().title()

#dividir el nombre del usuario en nombre y apellido
nombre, apellido, = nombre.split(" ")

#saludar al usuario
print(f"Hola, {nombre}")
