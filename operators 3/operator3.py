#printing is and is not

a=11.5
if(type(a)is float):
    print("true")
else:
    print("false")

x="pinapple"
y="pinapple"

if(x is y):
    print("the property is identical")
y="apple"
if(x is not y):
    print("there property is different")
