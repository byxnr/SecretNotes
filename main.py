from tkinter import *
import pybase64
from tkinter import messagebox

window = Tk()
window.title("Secret Notes")
window.minsize(width=300, height=500)
window.config(padx=30,pady=30)
window.config(bg="lavenderblush")
FONT = ("Verdena",12,"normal")

photo = PhotoImage(file= "secret.png")
photo_label = Label(image=photo)
photo_label.config(bg="lavenderblush")
photo_label.pack()

def clear():
    text.delete(1.0, END)
    entry_2.delete(0, END)
def encrypt():
    secrets = text.get(1.0, END)
    text.delete(1.0,END)
    entry_1.delete(0,END)
    if entry_2.get() == "beyza":
        secrets = secrets.encode("ascii")
        secrets = pybase64.b64encode(secrets)
        secrets = secrets.decode("ascii")
        text.insert(END, secrets)
        entry_2.delete(0,END)
        with open("mysecret.txt","a") as data_file:
            data_file.write(f"\n{text}\n{secrets}")
    else:
        messagebox.showwarning("Incorrect!", "Incorrect Password, Try Again!!")

def decrypt():
    secrets = text.get(1.0, END)
    text.delete(1.0, END)

    if entry_2.get() == "beyza":
        secrets = secrets.encode("ascii")
        secrets = pybase64.b64decode(secrets)
        secrets = secrets.decode("ascii")
        text.insert(END, secrets)
    else:nit
        messagebox.showwarning("Incorrect!", "Incorrect Password, Try Again!!")


label_1 = Label(text="Enter Your Title",font=FONT)
label_1.config(bg="palevioletred")
label_1.config(fg="white")
label_1.pack()

entry_1 = Entry(width=30)
entry_1.config(bg="aliceblue")
entry_1.pack()

label_2 = Label(text="Enter Your Secret", font=FONT)
label_2.config(bg="palevioletred")
label_2.config(fg="white")
label_2.pack()

text = Text(width=30, height=10)
text.config(bg="aliceblue")
text.pack()

label_3 = Label(text="Enter Master Key", font=FONT)
label_3.config(bg="palevioletred")
label_3.config(fg="white")
label_3.pack()

entry_2 = Entry(width=30)
entry_2.config(bg="aliceblue")
entry_2.pack()

button_1 = Button(text="Save & Encrypt",command=encrypt)
button_1.config(bg="palevioletred")
button_1.config(fg="white")
button_1.pack()

button_2 = Button(text="Decrypt",command=decrypt)
button_2.config(bg="palevioletred")
button_2.config(fg="white")
button_2.pack()

button_3 = Button(text="Clear",command=clear)
button_3.config(bg="palevioletred")
button_3.config(fg="white")
button_3.pack()


window.mainloop()