def computegrade (g):
    if 1>= g >= 0.9 :
            print ("A")

    elif 1> g >= 0.8:
                print ("B")

    elif 1> g >= 0.7:
                    print ("c")
    elif 1> g >= 0.6 :
                    print ("d")
    elif  0< g < 0.6:
                    print ("f")

    else:
                    print ("error")


s = input ("Enter Score: ")
try:
    score = float(s)
    computegrade(score)
except:
    print("Bad Score")
