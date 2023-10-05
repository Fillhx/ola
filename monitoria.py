estracto = int(input("INGRESE SU ESTRACTO: "))
valor_de_consumo = float(input("INGRESE SU VALOR DE CONSUMO: "))

valor_base = 0

if estracto == 1:
    valor_base == 500
elif estracto == 2:
    valor_base = 700
elif estracto == 3:
    valor_base = 4800
elif estracto == 4:
    valor_base = 6700
else:
    print("ingrese un valor valido")

internet = 0
aseo = 0

if (estracto>=1 and estracto <=4):
    internet = (20/100)* valor_de_consumo
    aseo = (12.2/100)* valor_de_consumo
else:
    print("ingrese un valor valido")

valor_factura = valor_base + valor_de_consumo + internet + aseo 
print(f"su valor toal de factura es: {valor_factura}")