import random 
while True:
    user=input('enter your choice (r,p,s): ')
    p_action=['r','s','p']
    computer_choice=random.choice(p_action)
    print('your choice was',user)
    print('computer choice was',computer_choice)
    if user==computer_choice:
        print('TIE')
    elif user=='r':
        if computer_choice=='s':
            print('you win')
        else:
            print('you lose it was papar')
    elif user=='s':
        if computer_choice=='p':
            print('you win')
        else:
            print('you lose it was r')
    elif user=='p':
        if computer_choice=='r':
            print('you win')
        else:
            print('you lose it was s')
    play_again=input('play again ?(y/n)')
    if play_again !='y':
        break
            