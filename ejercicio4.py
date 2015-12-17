"""4. Ampliació de l'exercici 3 però tractant el cas que siguin iguals."""
NUM = input("Introudiex el primer nombre:")
NUM = int(NUM)
NUM2 = input("Introdueix el segon nombre:")
NUM2 = int(NUM2)
if NUM > NUM2:
    print("El numero", NUM, "es mes gran que", NUM2)
elif NUM2 > NUM:
    print("El numero", NUM2, "es mes gran que", NUM)
else:
    print("El numero", NUM, "es igual que", NUM2)
