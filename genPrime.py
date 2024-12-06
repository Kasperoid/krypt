import time
import math

def isqrt(x):
    n = int(x)
    r = 1 << ((n.bit_length() + 1) >> 1)
    while True:
        newr = (r + n // r) >> 1  # next estimate by Newton-Raphson
        if newr >= r:
            return r
        r = newr


def is_prime(n):
    n = int(n)
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_PrimeMR(n):
    n = int(n)

    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False

    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for i in range(8):
        a = genN(2, n)
        if trial_composite(a):
            return False

    return True

def genProst(n):
    pr = int(time.time() * 1000000) % n
    while not is_prime(pr):
        pr = int(time.time() * 1000000) % n
    return pr

def genProst256():
    pr = genBit(255)
    while is_PrimeMR(pr) != True:
        pr = genBit(255)
    return pr
def genProst508_512():
    pr = genBit(genN(508, 511))
    while is_PrimeMR(pr) != True:
        pr = genBit(genN(508, 511))
    return pr

def gРеnN(a, b):
    n = int(time.time() * 1000000) % b
    while n < a:
        n = int(time.time() * 1000000) % b
    return n

def gРеnBit(n):
    b = []
    for i in range(n ):
        b.append(genN(0, 2))
        time.sleep(0.000003)
    return int('0b' + ''.join(str(x) for x in b), 2)

































#region г…¤
from random import randrange as genN # noinspection
from random import getrandbits as genBit # noinspection
#endregion # noinspection


































