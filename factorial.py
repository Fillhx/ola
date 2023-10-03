# def factorial(n):
#     if n < 0: return None
#     if n < 2: return 1
#     else:
#         return n * factorial(n-1)




# if __name__ == "__main__":
#     print(factorial())


def example(b):
    if b > 50:
        return 15
    else:
        return 2 + example(b + 23)

if __name__ == "__main__":
    b = int(input("ingrese un valor: "))
    print(example(b))