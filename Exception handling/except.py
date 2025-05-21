try:
    num1,num2=eval(input('enter a two number,s seperated by a comma: '))
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print('division ERROR!')
except SyntaxError:
    print('comma is missing')
except:
     print('value inavalid')
else:
    print('NO ERROR')
finally:
    print('this will come how ever you try to romove it')