num=[1,4,2,5,7,8]

target=int(input('enter a sum: '))
lookup={}
for i, num in enumerate(num):
    if target - num in lookup:
        print('found in index',lookup [target - num],"and",i)
        break
    lookup [num]=i
else:
    print("IVALID")
    