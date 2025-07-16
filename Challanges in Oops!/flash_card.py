class flash_card:
    def __init__(self,word,guess):
        self.word=word
        self.guess=guess
    def __str__(self):
        return self.word+' ( '+self.guess+' )'

flash=[]
print('welcometo flash! card game')
while True:
    word=input('enter the name u want to dispaly on the flash card')
    guess=input('enter the guess')
    flash.append(flash_card(word,guess))
    option=input('enter 0 if u want to add anothe flash card otherwise enter 1')
    if (option):
        break

print("\nYour flashcards")

for i in flash:
   print(i)   