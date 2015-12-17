"""6. Algorisme que llegeix 3 nombres i els mostra ordenats de major a menor."""
NUM = input("Introdueix el primer numero:")
NUM = int(NUM)
NUM2 = input("Introdueix el segon numero:")
NUM2 = int(NUM2)
NUM3 = input("Introdueix el tercer numero:")
NUM3 = int(NUM3)

if NUM > NUM2 and NUM > NUM3 and NUM2 > NUM3:
    print("Els numeros queden aixi ordenats", NUM, ">", NUM2, ">", NUM3)
elif NUM > NUM2 and NUM > NUM3 and NUM3 > NUM2:
    print("Els numeros queden aixi ordenats", NUM, ">", NUM3, ">", NUM2)
elif NUM2 > NUM and NUM2 > NUM3 and NUM > NUM3:
    print("Els numeros queden aixi ordenats", NUM2, ">", NUM, ">", NUM3)
elif NUM2 > NUM and NUM2 > NUM3 and NUM3 > NUM:
    print("Els numeros queden aixi ordenats", NUM2, ">", NUM3, ">", NUM)
elif NUM3 > NUM2 and NUM3 > NUM and NUM > NUM2:
    print("Els numeros queden aixi ordenats", NUM3, ">", NUM, ">", NUM2)
else:
    print("Els numeros queden aixi ordenats", NUM3, ">", NUM2, ">", NUM)

