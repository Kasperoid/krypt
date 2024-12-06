def mod_inverse(e, n):  # Нахождение значения из разряда e^-1
    """
        e: значение, для которого ищется обратное
        n: модуль
    """

    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    # Проверяем, что e и n взаимно просты
    gcd, x, _ = extended_gcd(e, n)

    if gcd != 1:
        raise ValueError("Мультипликативно обратное значение не существует")

    # Приводим результат к положительному значению по модулю n
    return x % n