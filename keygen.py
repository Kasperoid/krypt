import datetime
import ElipticFuncs
import genPrime
import test
# Формирование параметров схемы цифровой подписи

def keygen():

    # PARAMETRS_OBJ = {
    #     "gost-3410-12-512-paramSetA": {
    #         "p": "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDC7",
    #         "a": "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDC4",
    #         "b": "E8C2505DEDFC86DDC1BD0B2B6667F1DA34B82574761CB0E879BD081CFD0B6265EE3CB090F30D27614CB4574010DA90DD862EF9D4EBEE4761503190785A71C760",
    #         "q": "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF27E69532F48D89116FF22B8D4E0560609B4B38ABFAD2B85DCACDB1411F10B275",
    #         "x": "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003",
    #         "y": "7503CFE87A836AE3A61B8816E25450E6CE5E1C93ACF1ABC1778064FDCBEFA921DF1626BE4FD036E93D75E6A50E3A41E98028FE5FC235F5B889A589CB5215F2A4",
    #     },
    # }
    #
    # p = int(PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["p"], 16)
    #
    # a = int(PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["a"], 16)
    #
    # b = int(PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["b"], 16)
    #
    # q = int(PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["q"], 16)
    #
    # xp = int(PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["x"], 16)
    #
    # yp = int(PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["y"], 16)

    # p = genPrime.genProst(1000000000)
    # q = genPrime.genProst(10000000
    # a = genPrime.genN(0, p)
    # b = genPrime.genN(0, p)
    #
    # while (4 * (a**3) + 27 * (b**2)) % 2 == 0:
    #     b = genPrime.genN(0, p)
    # xp = 0
    # yp = 0
    # for xi in range(2, p):
    #     yi = ((xi ** 3 + a * xi + b) % p) ** 0.5
    #     if int(yi) == yi:
    #         xp = xi
    #         yp = int(yi)
    #         break

    p, q, a, b, xp, yp = test.generate_parameters()

    #### Формирование ключа подписи d


    d = 0

    while True:
        current_time = str(datetime.datetime.now())
        result = hash(current_time) % q
        if (result > 0 and result < q):
            d = result

            break

    #### Формирвоание ключа проверки подписи

    xq, yq = ElipticFuncs.scalar_multiply(d,[xp, yp], p, a)
    return p, a, b, q, xp, yp, d, xq, yq