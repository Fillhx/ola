#tablas

contador1 = 2


while contador1 <= 11:
    print(f"la tabla del numero {contador1}")
    contador2 = 1
    si = 0
    while contador2 <= 12:
        print(str (contador1)  + "x" + str(contador2) + "="+ str(contador1  * contador2))
        si += contador1 * contador2
        contador2 += 1
    
    print("el total es", si)
    contador1 += 1

