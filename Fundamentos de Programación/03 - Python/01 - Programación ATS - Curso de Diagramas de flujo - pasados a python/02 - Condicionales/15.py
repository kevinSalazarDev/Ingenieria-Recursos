# 15. Hacer un programa que simule el lanzamiento de una moneda.

import random


numero = random.randint(0,1)

if numero == 0:
    print("Cara")

else:
    print("Sello")