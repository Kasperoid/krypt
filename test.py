from decimal import *
getcontext().prec = 1000
def sqrt_big(n):
    if n < 0:
        return None
    if n == 0:
        return Decimal(0)
    x = Decimal(n)
    y = (x + 1) / 2

    while abs(y - x) > Decimal('1e-1000'):
        x = y
        y = (x + n / x) / 2
        return y