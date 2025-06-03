def word_count(words):
    ctr=0
    list=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            list.append(word)
    print(list)
    return ctr
count=word_count(["aca","dfg","cac","pyp"])
print(count)

    