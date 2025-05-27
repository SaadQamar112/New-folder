import random
playing=True
number=str(random.randint(0,15))

print('guss the number till o to 15')
print('you will win ame when you will guss the right anwer')

while playing:
    guss=input('enter you guss:')
    if number==guss:
        print('you got the number right')
        print('number=',number)
        break
    else:
        print('you got the number wrong')
        