try:
    n=int(input('enter your age: '))
    print(n)
except ValueError:
    print('INVALID')
if n%2==0:
    print("its a even number")
else:
    print("its a odd number")