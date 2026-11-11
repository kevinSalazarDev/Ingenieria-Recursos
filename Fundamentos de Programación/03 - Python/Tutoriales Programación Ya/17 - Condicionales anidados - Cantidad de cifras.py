num = int(input("Ingrese un número positivo de hasta tres cifras: "))

if 1 <= num <= 9:
    print("El número tiene 1 cifra")
elif 10 <= num <= 99:
    print("El número tiene 2 cifras")
elif 100 <= num <= 999:
    print("El número tiene 3 cifras")
else:
    print("Error: ingrese un número positivo de hasta tres cifras.")
