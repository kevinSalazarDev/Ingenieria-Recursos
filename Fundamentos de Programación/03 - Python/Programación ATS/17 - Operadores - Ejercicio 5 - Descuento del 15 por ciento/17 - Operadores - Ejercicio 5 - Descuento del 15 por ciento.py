# Una tienda ofrece un descuento del 15% sobre el total de la compra y un
# cliente desea saber cuánto deberá pagar finalmente por su compra

total_compra = float(input("Ingrese el total de la compra: "))

descuento = total_compra*15/100
total_pagar = total_compra - descuento

print(f"El total a pagar es: ${total_pagar:.2f}")

