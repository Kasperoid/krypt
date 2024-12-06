import datetime
import GostHash
import ElipticFuncs

def sign(d, message, q, xp, yp, a, p):
    # Процесс формирования цифровой подписи
    # Исходные данные d и message

    xc = {
        "16": 0,
        "10": 0,
    }

    yc = {
        "16": 0,
        "10": 0,
    }

    e = {
        "16": 0,
        "10": 0,
    }

    k = {
        "16": 0,
        "10": 0,
    }

    r = {
        "16": 0,
        "10": 0,
    }

    s = {
        "16": 0,
        "10": 0,
    }

    h = GostHash.entry().FromString(message, 512)

    alpha = int(h, 16)

    if (alpha % q["10"] == 0):
        e["10"] = 1
        e["16"] = hex(1)
    else:
        e["10"] = alpha % q["10"]
        e["16"] = hex(alpha % q["10"])

    while True:
        current_time = str(datetime.datetime.now())
        result = hash(current_time) % q["10"]
        if (result > 0 and result < q["10"]):
            k["10"] = result
            k["16"] = hex(result)

            xc["10"], yc["10"] = ElipticFuncs.scalar_multiply(k["10"], [xp["10"], yp["10"]], p["10"], a["10"])
            xc["16"] = hex(xc["10"])
            yc["16"] = hex(yc["10"])

            r["10"] = xc["10"] % q["10"]
            r["16"] = hex(xc["10"] % q["10"])

            if r["10"] != 0:

                s["10"] = (r["10"] * d["10"] + k['10'] * e["10"]) % q["10"]
                s["16"] = hex((r["10"] * d["10"] + k['10'] * e["10"]) % q["10"])
                if s["10"] != 0:
                    break
    return r, s