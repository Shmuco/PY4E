hrs = input("Enter Hours:")
rte = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rte)
except: print(" Error, please enter numeric input")

hrs = input("Enter Hours:")
rte = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rte)
except: print(" Error, please enter numeric input")

if h > 40 :
     pay = (40 * r)+((h - 40) * r * 1.5)
else:
     pay = r * h
print (pay)
