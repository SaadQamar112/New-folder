list=[1,5,7,4,0,2]
print(list)

count=0
for i in list:
    count+=i

avrg=count/len(list)

print(avrg)
print(count)

list.sort()

print(list[0])
print(list[-1])
