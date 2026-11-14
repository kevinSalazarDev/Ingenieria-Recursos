# 9. Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se
# compran tres camisas o más se aplica un descuento del 20% sobre el total de la
# compra y si son menos de tres camisas un descuento del 10%

numero_camisa = int(input("Ingrese el número de camisas que compró: "))
precio_camisa = float(input("Ingrese el precio de cada camisa: "))

subtotal = numero_camisa*precio_camisa

if numero_camisa >= 3:
    descuento = subtotal*20/100
else:
    descuento = subtotal*10/100

total = subtotal - descuento    

print(f"El precio total es: ${total}")