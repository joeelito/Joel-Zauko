"""3. Algorisme que llegeix dos nombres i mostra com a resultat quin és el
    més gran."""
NUM = input("Introudiex el primer nombre:")
NUM = int(NUM)
NUM2 = input("Introdueix el segon nombre:")
NUM2 = int(NUM2)
if NUM > NUM2:
    print("El numero", NUM, "es mes gran que", NUM2)
else:
    print("El numero", NUM2, "es mes gran que", NUM)
