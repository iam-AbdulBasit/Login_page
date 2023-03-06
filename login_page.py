from tkinter import *

def login():
    username = username_entry.get()
    username = username_entry.get()
    if username == "Username" and password == "password":
        message_label.config(text="login successful")
    else:
        message_label.config(text="invalid user name and password")

root = Tk()
root.geometry("1000x900")

username_label = Label(root,text="Username:")
username_label.pack()
username_entry = Entry(root)
username_entry.pack()

password_label = Label(root,text="password:")
password_label.pack()
password_entry = Entry(root,show="*")
password_entry.pack()

login_button = Button(root,text="Login",command=login)
login_button.pack()

message_label = Label(root)
message_label.pack()

root.mainloop()
