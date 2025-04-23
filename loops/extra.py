text=str(input("enter a sentence:  "))
text=text.split()
bigwordlen=0
for wrd in text:
    wrdlen=len(wrd)
if wrdlen>bigwordlen:
    bigwordlen=wrdlen
print("\n print largest word")
for wrd in text:
    wrdlen=len(wrd)
if wrdlen==bigwordlen:
    print(wrd)