

ola = int(input("ingrese su edad: "))
print("escoga su genero:\n 1.M \n 2.F" )
ola_2 = int(input("escoja el numero que corresponde a su genero:"))
ola_3 = int(input("ingrese su estracto social: "))

if ola >= 18:
    print("segun tu edad, tu eres mayor de edad")
# elif ola < 18:
else:
    print("segun tu edad, sos menorcito, pero toca respetarte")


if ola_2 == 1 or ola_2 == 2:
    print("segun tu genero, eres una persona normal (gracias a dios)")
# elif ola_2 <1 or ola_2>2:
else:
    print("eso existe?, sos un robot o que")

if ola_3 == 1:
    print("estracto 2?, pobre de mrda")
elif ola_3 == 2:
    print("estracto 2?, pues ni pobre ni rico")
elif ola_3 > 3 and ola_3 < 5:
    print("mano, vos con ese estracto andas luqueado")
else:
    print("mlparido bañado en plata")


