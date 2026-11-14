'''
11. Calcular el total que una persona debe pagar en una llantera, si el precio de
cada llanta es de $800 si se compran menos de 5 llantas y de $700 si se compran
5 o más.

'''

numero_llantas = int(input("Ingrese el número de llantas que comprará: "))

if numero_llantas >= 5:
    total = numero_llantas*700

else:
    total = numero_llantas*800

print(f"El precio total es: ${total}")