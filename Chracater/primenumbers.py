lower=int(input("enter a lower case:  "))
upper=int(input("enter a upper case:"))
print("print prime number between",lower,upper )
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num % i)== 0:
                break
        else:
            print(num)