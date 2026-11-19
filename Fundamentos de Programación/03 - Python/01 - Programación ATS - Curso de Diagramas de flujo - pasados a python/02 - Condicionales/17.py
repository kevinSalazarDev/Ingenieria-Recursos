''' 
17. En una tienda de descuento se efectúa una promoción en la cual se hace un
descuento sobre el valor de la compra total según el color de la bolita que el
cliente saque al pagar en caja. Si la bolita es de color blanco no se le hará
descuento alguno, si es verde se le hará un 10% de descuento, si es amarilla un
25%, si es azul un 50% y si es roja un 100%. Se sabe que solo hay bolitas de los
colores mencionados.

'''

import random


compra = float(input("Ingrese el valor de su compra: "))

r = random.randint(1,5)

if r == 1:
    print("Bolita blanca")
    descuento = compra
    print("No obtuvo un descuento")

elif r == 2:
    print("Bolita verde")
    descuento = compra*10/100

elif r == 3:
    print("Bolita amarilla")
    descuento = compra*25/100

elif r == 4:
    print("Bolita azul")    
    descuento = compra*50/100

else:
    print("Bolita roja")
    descuento = compra*100/100

total = compra - descuento    
print(f"El total es: ${total} ")


