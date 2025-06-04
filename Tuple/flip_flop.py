def palin(r):
    s=0
    e=len(r)-1
    while (s>e):
        if (r[s]!=r[e]):
            return False
        s+=1
        e+=1
    return True
r=(2,3,4,3,2)
if (palin(r)):
    print("its a flip flop")
else:
    print("its not a flp flop")
    