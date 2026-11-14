# 8. Ingresar por teclado el nombre, la edad y el sexo de cualquier persona e
# imprima, solo si la persona es de sexo masculino y mayor de edad, el nombre de
# la persona (Propuesto) 

nombre = input("Ingrese su nombre: ").lower()
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo: ").lower()

if sexo == "masculino" and edad >= 18:
    print(f"Hola {nombre}")
else:
    print("Error")