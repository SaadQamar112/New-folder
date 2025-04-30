string=(input("enter your own word:  "))
chrac=(input("enter your own charcater:  "))
i=0
count=0
while(i<len(string)):
    if(string[i]==chrac):
        count=count+1
    i=i+1
print("",chrac,count)
