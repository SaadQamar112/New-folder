def hotelcost(nights):
    return 140*nights #$
def planecost(city):
    if "los angolus"==city:
        return 475
    elif "dubai"==city:
        return 500
    elif "pakistan"==city:
        return 250
def rentalcar(days):
    if days>=7:
        return 35*days
    else:
        return 40*days
def wholetrip(city,days,spendingmoney):
    return rentalcar(days)+hotelcost(days)+planecost(city)+spendingmoney
print(rentalcar(5))
print(hotelcost(3))
print(planecost("dubai"))
print(wholetrip("dubai",5,5000))
    
     