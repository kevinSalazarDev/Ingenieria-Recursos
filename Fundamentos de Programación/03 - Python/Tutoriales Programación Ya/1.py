def calcular_total(precio, cantidad):
    return precio * cantidad


precio = float(input("Ingrese el precio del producto: "))
cantidad = 3

resultado = calcular_total(precio, cantidad)

print("El total de la compra es:", resultado)
