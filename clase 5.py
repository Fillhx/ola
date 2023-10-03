def is_triangle(a, b ,c): #solo permite mencionar si es o no un triangulo, es una auxiliar
    return a + b > c and a + c > b and b + c > a


def is_rectangle(a, b, c):
    if not is_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    # if b > a and b > c:
    #     return False
    # if a == b and b == c and a == c:
    #     return False
    else:
        return False


if __name__ == "__main__":
    print(is_rectangle(3, 4, 5))
    print(is_rectangle(1, 1, 1))
    print(is_rectangle(3, 4, 2))