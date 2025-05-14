def bill_tipper(billamount,tippercent):
    total=billamount*(1+0.01 * tippercent)
    total=round(total,2)
    print("plz pay your bill",total)

bill_tipper(130,20)
