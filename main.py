import datetime

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

PARAMETRS_OBJ = {
    "gost-3410-12-512-paramSetA": {
        "p": "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDC7",
        "a": "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDC4",
        "b": "E8C2505DEDFC86DDC1BD0B2B6667F1DA34B82574761CB0E879BD081CFD0B6265EE3CB090F30D27614CB4574010DA90DD862EF9D4EBEE4761503190785A71C760",
        "q": "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF27E69532F48D89116FF22B8D4E0560609B4B38ABFAD2B85DCACDB1411F10B275",
        "x": "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003",
        "y": "7503CFE87A836AE3A61B8816E25450E6CE5E1C93ACF1ABC1778064FDCBEFA921DF1626BE4FD036E93D75E6A50E3A41E98028FE5FC235F5B889A589CB5215F2A4",
    },
    "gost-3410-12-512-paramSetВ": {
        "p": "8000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006F",
        "a": "8000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006C",
        "b": "687D1B459DC841457E3E06CF6F5E2517B97C7D614AF138BCBF85DC806C4B289F3E965D2DB1416D217F8B276FAD1AB69C50F78BEE1FA3106EFB8CCBC7C5140116",
        "q": "800000000000000000000000000000000000000000000000000000000000000149A1EC142565A545ACFDB77BD9D40CFA8B996712101BEA0EC6346C54374F25BD",
        "x": "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002",
        "y": "1A8F7EDA389B094C2C071E3647A8940F3C123B697578C213BE6DD9E6C8EC7335DCB228FD1EDF4A39152CBCAAF8C0398828041055F94CEEEC7E21340780FE41BD",
    }
}

# Формирование параметров схемы цифровой подписи

p = {
    "16": PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["p"],
    "10": int(PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["p"], 16)
}

a = {
    "16": PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["a"],
    "10": int(PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["a"], 16)
}

b = {
    "16": PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["b"],
    "10": int(PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["b"], 16)
}

q = {
    "16": PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["q"],
    "10": int(PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["q"], 16)
}

xp = {
    "16": PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["x"],
    "10": int(PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["x"], 16)
}

yp = {
    "16": PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["y"],
    "10": int(PARAMETRS_OBJ["gost-3410-12-512-paramSetA"]["y"], 16)
}

#### Формирование ключа подписи d

d = {
    "16": 0,
    "10": 0,
}

while True:
    current_time = str(datetime.datetime.now())
    result = hash(current_time) % q["10"]
    if (result > 0 and result < q["10"]):
        d = {
            "16": hex(result),
            "10": result
        }
        break

#### Формирвоание ключа проверки подписи

xq = {
    "16": 0,
    "10": 0,
}

yq = {
    "16": 0,
    "10": 0,
}

xq["10"], yq["10"] = scalar_multiply(d["10"], [xp["10"], yp["10"]], p["10"], a["10"])
xq["16"] = hex(xq["10"])
yq["16"] = hex(yq["10"])

