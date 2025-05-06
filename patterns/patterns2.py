r=int(input("enter a number of rows:  "))
number=1
for i in range(1,r+1):
    for j in range(1,i+1):
        print(number,end="")
        number=number+1
    print()