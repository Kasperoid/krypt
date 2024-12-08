import random

def is_prime(n, k=5):  # Тест на простоту
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1  # Убедиться что число нечетное и имеет нужную длину
        if is_prime(num):
            return num

def generate_parameters():
    p = generate_prime(512)  # Простое большое число
    q = generate_prime(512)  # Меньшее простое число

    # Примерно определяем a и b для кривой. Измените под свои требования.
    a = random.randint(0, p - 1)
    b = random.randint(0, p - 1)

    # Генерация точки (x, y)
    while True:
        x = random.randint(0, p - 1)
        y2 = (x**3 + a * x + b) % p
        y = pow(y2, (p + 1) // 4, p)
        if (y * y) % p == y2:  # Проверка на принадлежность к кривой
            break

    return p, q, a, b, x, y