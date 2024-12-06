import keygen
import sign
import verif
def main():
    p, a, b, q, xp, yp, d, xq, yq = keygen.keygen()
    message = 'Test'
    r, s = sign.sign(d, message, q, xp, yp, a, p)
    print(verif.verif(message, r, s, q, p, xp, yp, a, xq, yq))

main()