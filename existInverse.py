import GostHash
import modInverse
def existInverse(message, q, p , xp, yp, a):
    ####### Проверка цифровой подписи

    e_prov = 0
    v = 0
    z1 = 0
    z2 = 0
    xc_prov = 0
    yc_prov = 0
    R = 0

    h_prov = GostHash.entry().FromString(message, 256)

    alpha_prov = int(h_prov, 16)

    if (alpha_prov % q == 0):
        e_prov = 1
    else:
        e_prov = alpha_prov % q

    v = modInverse.mod_inverse(e_prov, q) % q

    return v