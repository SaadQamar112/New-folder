num=int(input("declare a three digit number:  "))
sum=0
temp=num
while (temp>0):
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if num==sum:
    print("\n",num," is an armstrong number")
else:
    print("\n",num,"is not a armstrong number")
  