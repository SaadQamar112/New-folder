valid=False
while not valid:
    try:
        n=int(input("enter a even number: "))
        while n%2==0:
            print('hi')
        valid=True
    except SyntaxError:
        print("IVALID")
        