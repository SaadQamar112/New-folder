class computer:
    def __init__(self):
        self.__maxprice=30000
    def sell(self):
        print('',self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice=price
obj=computer()
obj.sell()
obj.setmaxprice(40000)
obj.sell()
