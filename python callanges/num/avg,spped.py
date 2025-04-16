a1=int(input("enter a value"))
b1=int(input("enter a value 2"))
c1=int(input("enter a value 3"))

avg=(a1+b1+c1)/3
print(avg)

if avg > a1 and avg > b1 and avg > c1:
    print("%d higher than %d,%d,%d"%(avg,a1,b1,c1))
elif avg > a1 and avg > b1:
    print("%d higher than %d,%d"%(avg,a1,b1))
elif avg > b1 and avg > c1:
    print("%d higher than %d,%d"%(avg,b1,c1))
elif avg > a1 and avg > c1:
    print("%d higher than %d,%d"%(avg,a1,c1))
else:
    print("IVALID INPUT")
