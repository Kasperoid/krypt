import datetime
import GostHash
import ElipticFuncs

def sign(d, message, q, xp, yp, a, p):
    # Процесс формирования цифровой подписи
    # Исходные данные d и message

    h = GostHash.entry().FromString(message, 512)

    alpha = int(h, 16)

    if (alpha % q == 0):
        e = 1
    else:
        e = alpha % q

    while True:
        current_time = str(datetime.datetime.now())
        result = hash(current_time) % q
        if (result > 0 and result < q):
            k = result

            xc, yc = ElipticFuncs.scalar_multiply(k, [xp, yp], p, a)

            r = xc % q

            if r != 0:

                s = (r * d + k * e) % q
                if s != 0:
                    break
    return r, s