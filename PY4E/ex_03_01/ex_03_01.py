hrs = input("Enter Hours:")
rte = input("Enter Rate:")

h = float(hrs)
r = float(rte)

if h > 40 :
     pay = (40 * r)+((h - 40) * r * 1.5)
else:
     pay = r * h
print (pay)
