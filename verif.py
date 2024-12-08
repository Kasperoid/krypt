import GostHash
import ElipticFuncs
import modInverse
def verif(message, r, s, q, p , xp, yp, a, xq, yq):
    ####### Проверка цифровой подписи

    e_prov = 0
    v = 0
    z1 = 0
    z2 = 0
    xc_prov = 0
    yc_prov = 0
    R = 0

    h_prov = GostHash.entry().FromString(message, 512)

    alpha_prov = int(h_prov, 16)

    if (alpha_prov % q == 0):
        e_prov = 1
    else:
        e_prov = alpha_prov % q

    v = modInverse.mod_inverse(e_prov, q) % q

    z1= (s * v) % q

    z2 = (-r * v) % q

    xc_prov, yc_prov = ElipticFuncs.add_points(ElipticFuncs.scalar_multiply(z1, [xp, yp], p, a), ElipticFuncs.scalar_multiply(z2, [xq, yq], p, a), p, a)

    R = xc_prov % q

    return R == r