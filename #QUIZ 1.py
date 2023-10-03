#QUIZ 1
#Integrante: Gustavo Muñoz (2380618)
#Docente: Luis Germán Toro Pareja
    
    
estracto = int (input("enter your social strate: "))
worth = float(input("enter your consumption value: "))
precio_base = worth * .20
precio_base2 = worth * .12

if estracto == 1:
    print("the value of your total invoice is:", worth + precio_base + precio_base2 + 500)
elif estracto == 2:
    print("the value of your total invoice is:", worth + precio_base + precio_base2 + 700)
elif estracto == 3:
    print("the value of your total invoice is", worth + precio_base + precio_base2 + 4800)
elif estracto == 4:
    print("the value of your total invoice is", worth + precio_base + precio_base2 + 6700)

else:
    print("enter a valid value")








