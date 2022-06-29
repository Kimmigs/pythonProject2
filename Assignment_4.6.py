hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)

def computepay(h, r):
    regh = 40
    oth = h % regh
    otr = r * 1.5
    if h <= 40:
        pay = h * r
    else:
        pay = regh * r + oth * otr
    return pay
p = computepay(h, r)
print("Pay", p)
