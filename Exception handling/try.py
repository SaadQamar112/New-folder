try:
    number=int(input("enter a number: "))
    print("number is : ",number)
except ValueError as ex:
    print(ex)
    