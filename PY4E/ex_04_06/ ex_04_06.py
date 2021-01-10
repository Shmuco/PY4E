def computepay(h,r):
    print("In computepay", h, r)
    if h > 40 :
         pay = (40 * r)+((h - 40) * r * 1.5)
    else:
         pay = r * h
    print ("Returning",pay)
    return pay



hrs = input("Enter Hours:")
rte = input("Enter Rate:")

xh = float(hrs)
xr = float(rte)

xp = computepay(xh,xr)

print("Pay:",xp )
