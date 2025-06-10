dict={'id1':
{'name':['Saad'],
 'class':['VIII'],
 'subject':['computer,english']},
'id2':{'name':['ammar'],
       'class':['VII'],
       'subject':['science,physics']
},
'id3':
{'name':['Saad'],
 'class':['VIII'],
 'subject':['computer,english']},
}

result={}
for key,value in dict.items():
    if value not in result.values():
        result[key]=value
print(result)
