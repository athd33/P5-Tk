from tkinter import messagebox, Tk, Frame, Label, Button, Entry, StringVar

from functions import quitt_app, is_valid_register, insert_register_infos
import sys 


root=Tk() # main window
root.geometry("950x950+550+250")
root.title("** P5 -- FOOD SEARCH APP -- ")
root.geometry("800x700+400+300")

HomePage = Frame(root)  # frames
LoginPage = Frame(root)
RegisterPage = Frame(root)


def raise_frame(frame):
    frame.tkraise()


for frame in(HomePage,LoginPage,RegisterPage):
    frame.grid(row=0, column=0, sticky='news')

# HOME PAGE
Label(HomePage, text='HOME').grid(row=0, column=0, padx=370, pady=50)
Button(HomePage, text="Register", command=lambda:raise_frame(RegisterPage)).grid(row=1, column=0, pady=5)
Button(HomePage, text="Login", command=lambda:raise_frame(LoginPage)).grid(row=2, column=0, pady=5)
Button(HomePage, text="Quit", command=lambda:quitt_app()).grid(row=3, column=0, pady=5)


#REGISTER PAGE
Label(RegisterPage, text='REGISTER').grid(row=0, column=0, padx=370, pady=5)
Label(RegisterPage, text="Enter username").grid(row=1, column=0, pady=2)
username = StringVar()
Entry(RegisterPage, textvariable=username).grid(row=2, column=0, pady=2)
Label(RegisterPage, text="Password").grid(row=3, column=0, pady=2)
psswd = StringVar()
Entry(RegisterPage, show="*", textvariable=psswd).grid(row=4, column=0, pady=2)
Label(RegisterPage, text="Confirm password").grid(row=5, column=0, pady=2)
confirm = StringVar()
Entry(RegisterPage, show="*", textvariable=confirm).grid(row=6, column=0, pady=2)
Button(RegisterPage, text="SUBMIT", command=lambda:check_register_info(username.get(),
                                                                   psswd.get(),
                                                                   confirm.get())).grid(row=7, column=0, pady=5)
Button(RegisterPage, text="Home", command=lambda:raise_frame(HomePage)).grid(row=8, column=0, pady=5)
Button(RegisterPage, text="Login", command=lambda:raise_frame(LoginPage)).grid(row=9, column=0, pady=5)
Button(RegisterPage, text="Quit", command=lambda:quitt_app()).grid(row=10, column=0, pady=5)


#LOGIN PAGE
Label(LoginPage, text='LOGIN').grid(row=0, column=0, padx=370, pady=5)
Label(LoginPage, text="Enter username").grid(row=1, column=0, pady=2)
Entry(LoginPage).grid(row=2, column=0, pady=2)
Label(LoginPage, text="Enter password").grid(row=3, column=0, pady=2)
Entry(LoginPage, show="*").grid(row=4, column=0, pady=2)
Button(LoginPage, text="Submit").grid(row=5, column=0, pady=5)
Button(LoginPage, text="Home", command=lambda:raise_frame(HomePage)).grid(row=6, column=0, pady=5)
Button(LoginPage, text="Quit", command=lambda:quitt_app()).grid(row=7, column=0, pady=5)



def check_register_info(username,psswd, confirm):
    if is_valid_register(username,psswd, confirm):
        insert_register_infos(username, psswd)
        messagebox.showinfo("Regestered!", "Your account is created!")
        raise_frame(HomePage)
        

raise_frame(HomePage)
root.mainloop()
