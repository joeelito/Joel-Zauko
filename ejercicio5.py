"""5. Algorisme que llegeix 3 nombres i diu quin és el major."""
NUM = input("Introdueix el primer numero:")
NUM = int(NUM)
NUM2 = input("Introdueix el segon numero:")
NUM2 = int(NUM2)
NUM3 = input("Introdueix el tercer numero:")
NUM3 = int(NUM3)

if NUM > NUM2 and NUM > NUM3:
    print("El numero", NUM, "es el mes gran")
elif NUM2 > NUM and NUM2 > NUM3:
    print("El numero", NUM2, "es el mes gran")
else:
    print("El numero", NUM3, "es el mes gran")
