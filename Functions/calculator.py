def addition(P,Q):
    return P+Q
def subtraction(P,Q):
    return P-Q
def multiply(P,Q):
    return P*Q
def divide(P,Q):
    return P/Q

print("select whhich operation you want:")
print("a. addition")
print("b. subtraction")
print("c. multiply")
print("d. divide")

choice=input("please enter your choice (a.b.c.d): ")

num1=int(input("enter the first value"))
num2=int(input("enter the second value"))

if choice=='a':
    print(addition(num1,num2))
elif choice=='b':
    print(subtraction(num1,num2))
elif choice=='c':
    print(multiply(num1,num2))
elif choice=='d':
    print(divide(num1,num2))
else:
    print("INVALID INPUT")
    