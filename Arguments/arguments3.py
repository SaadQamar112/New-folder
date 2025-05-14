def factor(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factor(x-1)

print("factor of 2 is : ",factor(2))
print("factor of 5 is : ",factor(5))
print("factor of 9 is : ",factor(9))
