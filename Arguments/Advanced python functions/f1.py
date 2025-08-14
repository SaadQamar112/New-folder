num1=[3,3,7,8]
num2=[9,3,6,1]

result=map(lambda x,y:x+y,num1,num2)

print(list(result))

num3=[9,8,7,6]
def squr(n):
    return n*n
math=list(map(squr,num3))

print(math)
