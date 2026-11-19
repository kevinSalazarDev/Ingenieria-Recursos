# 12. En un almacén se hace un 20% de descuento a los clientes cuya compra
# supere los $100 ¿Cuál será la cantidad que pagara una persona por su
# compra? (Propuesto)

subtotal = int(input("Ingrese el valor de su compra: "))

if subtotal > 100:
    descuento = subtotal*20/100
    total = subtotal-descuento
    print(f"El total es: ${total}")

else:
    print("No obtuvo el descuento")


