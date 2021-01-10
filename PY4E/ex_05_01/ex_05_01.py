num = 0
tot = 0.0
while True:
    sval = input ("Enter number: ")
    if sval == "done" :
        break
    try:
        fnum = float (sval)
    except:
        print ("Enter only Number")
        continue

    num = num + 1

    #print (num)

    tot = tot + fnum

    #print (tot)

average = tot/num

print ('Average:', average, 'Total:', tot, 'Number: ', num)
