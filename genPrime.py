import math
import time

def trial_division_primality(n):
    """
    Тест пробных делений для проверки простоты числа
    """
    # Обработка малых чисел
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Быстрые проверки
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Проверка делителей до квадратного корня из n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def fermat_primality_test(n, k=10):
    """
    Тест Ферма для проверки простоты числа

    Параметры:
    n - число для проверки
    k - количество итераций теста
    """
    # Обработка малых чисел
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    # Тест Ферма
    for _ in range(k):
        # Выбираем случайное число a от 2 до n-2
        a = math.floor(time.time() * 100000) % (n-2)

        # Проверяем условие Ферма: a^(n-1) ≡ 1 (mod n)
        if pow(a, n - 1, n) != 1:
            return False

    return True

def genPrime():
    def sieve_of_eratosthenes_bit(n):
        sieve = bytearray((n // 8) + 1)

        def is_prime(num):
            return not (sieve[num // 8] & (1 << (num % 8)))

        def mark_composite(num):
            sieve[num // 8] |= 1 << (num % 8)

        mark_composite(0)
        mark_composite(1)

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime(i):
                for j in range(i * i, n + 1, i):
                    mark_composite(j)

        return [num for num in range(2, n + 1) if is_prime(num)]

    def divide_primes_by_mod_3():
        set1 = []
        set2 = []

        for prime in primes:
            if prime == 3:
                continue

            remainder = prime % 3

            if remainder == 1:
                set1.append(prime)
            elif remainder == 2:
                set2.append(prime)

        return set1, set2

    def create_prost():
        while True:
            index_1 = math.floor(time.time() * 100000) % len(mnoj1)
            time.sleep(0.01)
            index_2 = math.floor(time.time() * 100000) % len(mnoj2)

            prime = mnoj1[index_1] * mnoj2[index_2] * 2 + 1

            if trial_division_primality(prime) and fermat_primality_test(prime):
                return prime


    primes = sieve_of_eratosthenes_bit(100000)
    mnoj1, mnoj2 = divide_primes_by_mod_3()

    return create_prost()

def genRandomNum():
    def sieve_of_eratosthenes_bit(n):
        sieve = bytearray((n // 8) + 1)

        def is_prime(num):
            return not (sieve[num // 8] & (1 << (num % 8)))

        def mark_composite(num):
            sieve[num // 8] |= 1 << (num % 8)

        mark_composite(0)
        mark_composite(1)

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime(i):
                for j in range(i * i, n + 1, i):
                    mark_composite(j)

        return [num for num in range(2, n + 1) if is_prime(num)]

    def divide_primes_by_mod_3():
        set1 = []
        set2 = []

        for prime in primes:
            if prime == 3:
                continue

            remainder = prime % 3

            if remainder == 1:
                set1.append(prime)
            elif remainder == 2:
                set2.append(prime)

        return set1, set2

    def create_prost():
        index_1 = math.floor(time.time() * 100000) % len(mnoj1)
        time.sleep(0.01)
        index_2 = math.floor(time.time() * 100000) % len(mnoj2)

        prime = mnoj1[index_1] * mnoj2[index_2] * 2 + 1

        return prime


    primes = sieve_of_eratosthenes_bit(100000)
    mnoj1, mnoj2 = divide_primes_by_mod_3()

    return create_prost()