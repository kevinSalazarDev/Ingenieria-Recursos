'''
10. En un supermercado se hace una promoción, mediante la cual el cliente
obtiene un descuento dependiendo de un número que se escoge al azar. Si el
numero escogido es menor que 74 el descuento es del 15% sobre el total
de la compra, si es mayor o igual a 74 el descuento es del 20%. Obtener cuanto
dinero se le descuenta. (Propuesto)

'''

import random


subtotal = float(input("Ingrese el subtotal de la compra: "))

numero_azar = random.randint(1,100)

if numero_azar >= 74:
    descuento = subtotal*20/100
else: 
    descuento = subtotal*15/100

print(f"El descuento es: ${descuento}")

