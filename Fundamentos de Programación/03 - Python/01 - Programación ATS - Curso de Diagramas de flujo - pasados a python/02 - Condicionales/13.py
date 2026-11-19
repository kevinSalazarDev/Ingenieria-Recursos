# 13. Ecuaciones de Segundo Grado: Ax^2 + Bx + C

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

d = b**2-4*a*c

if d>0:
    r1 = (-b+(d**1/2))/(2*a)
    r2 = (-b-(d**1/2))/(2*a)
    print(f"Las respuestas son: {r1}{r2}")

elif d == 0:
    r1 = (-b)/(2*a)
    print(f"La ecuación tiene una solución real doble: {r1}")

else:
    print("La ecuación no tiene solución real")