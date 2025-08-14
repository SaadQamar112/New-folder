from tkinter import*
from datetime import date
root=Tk()
root.title("getting started with widgits")
root.geometry("400x300")
lbl=label(text="enter the text",fg="white",bg="yellow",height=1,width=300)
lbl_name=label(text="full name",fg="black",bg="white")
name_entry=Entry()
def display():
    name=name_entry.get()
    message="welcome to application \ntoday's date is "
    greet="hello"+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())


text_box=Text(height=3)
button=Button(text="begin",command=display,hieght=1,bg="black",fg="yellow")
lbl.pack()
label_name.pack()
name_entry.pack()
button.pack()
text_box.pack()
root.mainloop()
