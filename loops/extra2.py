str=str(input("enter a sentece:  "))
total=1
for i in range(len(str)):
    if (str[i]==''):
        total=total+1
print("",total)
