import tkinter as tk
from tkinter import *
from textblob import TextBlob

root = tk.Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")

def check_spelling():
    word = text_entry.get()
    a= TextBlob(word)
    right = str(a.correct())

    cs = Label(root,text="Correct spelling is:",font=("poppins",20),bg="#dae6f6",fg="#364971")
    cs.place(x=100,y=250)
    spell.config(text=right)

heading = Label(root,text="Check Spelling",font=("Trebuchet Ms",30,"bold"),bg="#dae6f6",fg="#364971")
heading.pack(pady=(50,0))

text_entry = Entry(root,justify="center",width=30,font=("poppins",20),bg="#fff",bd=2)
text_entry.pack(pady=10)
text_entry.focus()

button = Button(root,text="Check",command=check_spelling,font=("roboto",20,"bold"),fg="white",bg="darkgreen")
button.pack()

spell = Label(root,font=("poppins",20),bg="#dae6f6",fg="#364971")
spell.place(x=350,y=250)


root.mainloop()