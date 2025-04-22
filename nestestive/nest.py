#creating variables

i=(input("did you attend te the medical cost Y or N: "))
g=int(input("student medical atendence: "))

if i=="Y":
    print("allowed")
else:
   if g>=75:
    print("allowed")
   else:
      print("not allowed")
