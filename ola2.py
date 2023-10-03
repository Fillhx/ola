# pollito: se va a morir


# def ola(numero):
#     # *caso base
#     # print(numero,end = " * ") paso a paso
#     if numero == 1:
#         print(numero, end = " = ")
#         return 1
#     # *caso recursivo
#     else:
#         print(numero, end = " + ")
#         return numero + ola(numero - 1)
    

# if __name__ == "__main__":
#     print(ola(100))


# factorial que indique una multiplicacion de menor a mayor termino

# def factorial(numero):
#     if numero == 1:
#         print(numero, end = " = ")
#         return 1
#     else:
#         print(numero, end = " * ")
#         return f"{factorial(numero -1)} * {numero}"
    

# if __name__ == "__main__":
#     print(factorial(5))
# si es impar se multiplica por 3 y se suma 1 y si es par se divide por 

# def par(n):
#     # print(int(par))######
#     if n == 1:
#         return 1
#     else:
#         if(n%2 == 0):
#             return par(n/2)
#         else:
#             return par (n * 2 + 1)
    
# if __name__ == "__main__":
#     print(par(18))
        
    
#convertir enteros a binarios

# def binarios(n):
#     if n == 0:
#         return "0"
#     elif n == 1:
#         return "1"
#     else:
#         return binarios(n//2) + str(n%2)
    

# if __name__ == "__main__":
#     print(binarios(70))


    

