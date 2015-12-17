"""2. Algorisme que llegeix un nombre i ens indica si és major que 10 o no."""
NUM = input("Introdueix el numero:")
NUM = int(NUM)
if NUM > 10:
    print("El numero", NUM, "es mes gran que 10")
else:
    print("El numero", NUM, "es mes petit o igual a 10")
