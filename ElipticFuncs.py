def elliptic_curve_add(P, Q, a, p):
    """Сложение точек на эллиптической кривой y² = x³ + ax + b (mod p)"""
    if P is None:
        return Q
    if Q is None:
        return P
    if P[0] == Q[0] and P[1] == -Q[1] % p:
        return None
    if P == Q:
        m = (3 * P[0]**2 + a) * pow(2 * P[1], -1, p) % p # Вычисляем обратное по модулю
        x3 = (m**2 - 2 * P[0]) % p
        y3 = (m * (P[0] - x3) - P[1]) % p
        return (x3, y3)
    else:
        m = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, p) % p
        x3 = (m**2 - P[0] - Q[0]) % p
        y3 = (m * (P[0] - x3) - P[1]) % p
        return (x3, y3)


def elliptic_curve_multiply(P, d, a, p):
     """Скалярное умножение точки на эллиптической кривой"""
     result = None
     while d > 0:
         if d % 2 == 1:
             result = elliptic_curve_add(result, P, a, p)
         P = elliptic_curve_add(P, P, a, p)
         d //= 2
     return result