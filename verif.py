import GostHash
import ElipticFuncs
import modInverse
def verif(message, r, s, q, p , xp, yp, a, xq, yq):
    ####### Проверка цифровой подписи

    e_prov = {
        "10": 0,
        "16": 0
    }

    v = {
        "10": 0,
        "16": 0,
    }

    z1 = {
        "10": 0,
        "16": 0,
    }

    z2 = {
        "10": 0,
        "16": 0,
    }

    xc_prov = {
        "10": 0,
        "16": 0,
    }

    yc_prov = {
        "10": 0,
        "16": 0,
    }

    R = {
        "10": 0,
        "16": 0,
    }

    h_prov = GostHash.entry().FromString(message, 512)

    alpha_prov = int(h_prov, 16)

    if (alpha_prov % q["10"] == 0):
        e_prov["10"] = 1
        e_prov["16"] = hex(1)
    else:
        e_prov["10"] = alpha_prov % q["10"]
        e_prov["16"] = hex(alpha_prov % q["10"])

    v["10"] = modInverse.mod_inverse(e_prov["10"], q["10"]) % q["10"]
    v["16"] = hex(v["10"])

    z1["10"] = (s["10"] * v["10"]) % q["10"]
    z1["16"] = hex(z1["10"])

    z2["10"] = (-r["10"] * v["10"]) % q["10"]
    z2["16"] = hex(z2["10"])

    xc_prov["10"], yc_prov["10"] = ElipticFuncs.add_points(ElipticFuncs.scalar_multiply(z1["10"], [xp["10"], yp["10"]], p["10"], a["10"]), ElipticFuncs.scalar_multiply(z2["10"], [xq["10"], yq["10"]], p["10"], a["10"]), p["10"], a["10"])
    xc_prov["16"] = hex(xc_prov["10"])
    yc_prov["16"] = hex(yc_prov["10"])

    R["10"] = xc_prov["10"] % q["10"]
    R["16"] = hex(R["10"])

    return R["10"] == r["10"]