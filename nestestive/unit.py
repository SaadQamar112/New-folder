#printing electricity bill
surcharge=0
u=int(input("enter the electriccitybill: "))
amount=0
if (u<50):
    amount=u*2.60
    surcharge=25
elif (u<=100):
    amount=130+ ((u-50)*3.25)
    surcharge=35
elif (u<=200):
    amount=130+162.50+526+ ((u-200)*8.45)
    surcharge=75
totalamount= amount+surcharge
print("electricity Bill= ",totalamount)


