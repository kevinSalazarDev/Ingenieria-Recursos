# 16. Una distribuidora de motocicletas tiene una promoción de fin de año qque
# consiste en lo siguiente. Las motos marca Honda tienen un descuento del 5%, las
# marcas Yamaha del 8% y las Suzuki del 10%, las otras marcas 2%. (Propuesto)

precio = float(input("Ingrese el precio de la moto: "))
marca = input("Ingrese la marca de la moto: ").lower()

if marca == "honda":
   descuento = precio*5/100
   total = precio - descuento
    

elif marca == "yamaha":
   descuento = precio*8/100
   total = precio - descuento
   

elif marca == "suzuki":
   descuento = precio*10/100
   total = precio - descuento
   

else:
   descuento = precio*2/100
   total = precio - descuento
   

print(f"El precio es: ${total}")
