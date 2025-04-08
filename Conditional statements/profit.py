actualcost=int(input("please enter the actual cost"))
marketprice=int(input("please enter the the market price"))
if (marketprice>actualcost):
    amount=marketprice-actualcost
    print("profit is ",amount)
else :
    print("No profit")
    