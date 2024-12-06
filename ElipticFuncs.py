def add_points(P1, P2, p, a):
    """
    Сложение двух точек эллиптической кривой
    P1, P2 - точки в виде кортежей (x, y)
    p - модуль (простое число)
    a - коэффициент кривой y^2 = x^3 + ax + b
    """
    if P1 is None:
        return P2
    if P2 is None:
        return P1

    x1, y1 = P1
    x2, y2 = P2

    if x1 == x2 and y1 == y2:
        # Удвоение точки
        if y1 == 0:
            return None

        # Вычисление lambda = (3x^2 + a)/(2y)
        numerator = (3 * x1 * x1 + a) % p
        denominator = (2 * y1) % p
        # Модульное деление
        lam = (numerator * pow(denominator, p - 2, p)) % p

    else:
        # Сложение разных точек
        if x1 == x2:
            return None

        # Вычисление lambda = (y2-y1)/(x2-x1)
        numerator = (y2 - y1) % p
        denominator = (x2 - x1) % p
        # Модульное деление
        lam = (numerator * pow(denominator, p - 2, p)) % p

    # Вычисление координат результирующей точки
    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return (x3, y3)


def scalar_multiply(k, P, p, a):
    """
    Умножение точки на число (scalar multiplication)
    k - множитель (целое число)
    P - точка эллиптической кривой в виде кортежа (x, y)
    p - модуль (простое число)
    a - коэффициент кривой
    """
    if k == 0:
        return None
    if k == 1:
        return P
    if k < 0:
        k = -k
        P = (P[0], (-P[1]) % p)

    # Метод двоичного разложения числа
    result = None
    addend = P

    while k:
        if k & 1:  # если текущий бит равен 1
            result = add_points(result, addend, p, a)
        addend = add_points(addend, addend, p, a)
        k >>= 1  # сдвиг вправо на 1 бит

    return result