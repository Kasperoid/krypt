import ElipticFuncs
import genPrime
import time
import math
# Формирование параметров схемы цифровой подписи

def keygen():
    p = 0
    xp = 0
    a = 0
    b = 0
    yp = 0
    q = 0
    d = 0
    xq = 0
    yq = 0

    while True:
        p = genPrime.genPrime()
        if (p % 4 == 3):
            break
    while True:
        a = math.floor(time.time() * 10000) % p
        if (a != 0 and a < p):
            break

    time.sleep(0.1)

    while True:
        b = math.floor(time.time() * 10000) % p
        if (b != 0 and b < p):
            break

    while (4 * (a ** 3) + 27 * (b ** 2)) % p == 0:
        time.sleep(0.01)
        b = math.floor(time.time() * 10000) % p

    for x1 in range(2, p):
        y1 = ((x1 ** 3 + a * x1 + b) % p) ** 0.5
        if int(y1) == y1:
            xp = x1
            yp = int(y1)
            break

    for q in range(int(p + 1 - 2 * (p ** 0.5)), int(p + 1 + 2 * (p ** 0.5))):
        if ElipticFuncs.elliptic_curve_multiply([xp, yp], q, a, p) == None:
            break

    while True:
        d = math.floor(time.time() * 10000) % q
        if (d > 2 and d < q):
            break

    xq, yq = ElipticFuncs.elliptic_curve_multiply([xp, yp], d, a, p)

    return p, a, b, q, xp, yp, d, xq, yq