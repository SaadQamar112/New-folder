print("enter your marks in 3 subjects")
subj1=int(input("englis"))
subj2=int(input("math"))
subj3=int(input("computer"))

total=subj1+subj2+subj3

avg=total/3

if avg>=91 and avg<100:
    print("you got A+")
elif avg>=81 and avg<91:
    print("you got A")
elif avg>=71 and avg<81:
    print("you got B+")
elif avg>=61 and avg<71:
    print("you got B")
elif avg>=51 and avg<61:
    print("you got C")
elif avg>=41 and avg<51:
    print("you got D")
else:
    print("invalid input")
    