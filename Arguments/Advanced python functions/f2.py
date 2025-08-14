function1={1,5,7,8}
function2={'w','x','y','z'}

result=list(zip(function1,function2))
print(result)

number1=[12,21,31,41]
number2=[41,31,21,12]

for x,y in zip(number1,number2[::-1]):
    print(x,y)


game=['xbox','PS','microsft ps']
price=[100000,200000,1200000]

new_dict={game:price for game,price in zip(game,price)}
print('/n{}'.format(new_dict))
