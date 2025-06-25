import random
import time 

number=random.randint(1,100)

def introduction():
    print('may i ask you your name')
    global name
    name=str(input())
    print(name+"we are oing to play a game i will guss a number betwwen 1 to 100")
    if number%2==0:
        x='even'
    else:
        x='odd'
    print('/n this is an {} number'.format(x))
    time.sleep(.5)
    print('go ahead .guess')

def pick():
    gussestaken=0
    while gussestaken<6:
        time.sleep(.25)
        enter=input("guess: ")
        try:
            guess=int(enter)
            if guess < 100 and guess > 1:
                gussestaken=gussestaken+1
                if gussestaken<6:
                    if guess < number:
                        print('the number is to low')
                    if guess > number :
                        print('number is to high')
                    if guess!=number:
                        print('try again')
                    if guess==number:
                        break
            if guess > 100 or guess < 1:
                print('number is not in the range')
                time.sleep(.25)
                print('guess a number between 1 to 100')
        except:
            print('i dont think it is a number sorry')
    if guess== number:
        gussestaken=str(gussestaken)
        print('good job {} you have guessed the number in {} guesses'.format(name,gussestaken))
    if guess!=number:
        print('this not the that i was thinking')
playagain='yes'
while playagain=='yes'or playagain=='y'or playagain=='Yes':
    introduction()
    pick()
    print('do you want to playagain')
    playagain=input()
    