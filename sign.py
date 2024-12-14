import datetime
import GostHash
import ElipticFuncs
import math
import time

def sign(d, message, q, xp, yp, a, p):
    # Процесс формирования цифровой подписи
    # Исходные данные d и message

    h = GostHash.entry().FromString(message, 256)

    alpha = int(h, 16)

    if (alpha % q == 0):
        e = 1
    else:
        e = alpha % q

    while True:
        k = 0
        while True:
            k = math.floor(time.time() * 10000) % q
            if (k > 2 and k < q):
                break

        xc, yc = ElipticFuncs.elliptic_curve_multiply([xp, yp], k, a, p)

        r = xc % q

        if (r != 0):
            s = (r * d + k * e) % q
            if s != 0:
                return r, s



    # while True:
    #     current_time = str(datetime.datetime.now())
    #     print(datetime.datetime.now())
    #     result = hash(current_time) % q
    #     if (result > 0 and result < q):
    #         k = result
    #
    #         xc, yc = ElipticFuncs.elliptic_curve_multiply([xp, yp], k, a, p)
    #
    #         r = xc % q
    #
    #         if r != 0:
    #
    #             s = (r * d + k * e) % q
    #             if s != 0:
    #                 break
    return r, s