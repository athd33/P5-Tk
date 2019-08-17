from tkinter import messagebox, Tk, Frame, Label, Button, Entry, StringVar, LabelFrame

from functions import quitt_app, is_valid_register, insert_register_infos, is_valid_login
import sys 


root=Tk() # main window
root.geometry("600x400+50+50")
root.title("** P5 -- FOOD SEARCH APP -- ")
root.geometry("800x600+400+300")

HomePage = Frame(root)  # frames
LoginPage = Frame(root)
RegisterPage = Frame(root)
CategoryPage = Frame(root)


def raise_frame(frame):
    frame.tkraise()


for frame in(HomePage, LoginPage, RegisterPage, CategoryPage):
    frame.grid(row=0, column=0, sticky='news')

# HOME PAGE
Label(HomePage, text='', bg='green', width=30).grid(row=0, column=0, pady=50)
Label(HomePage, text='HOME', bg='blue', width=40).grid(row=0, column=1, pady=50)
Label(HomePage, text='', bg='red', width=30).grid(row=0, column=2, pady=50)

Button(HomePage, text="Register", command=lambda: raise_frame(RegisterPage)).grid(row=1, column=1, pady=5)
Button(HomePage, text="Login", command=lambda: raise_frame(LoginPage)).grid(row=2, column=1, pady=5)
Button(HomePage, text="Quit", command=lambda: quitt_app()).grid(row=3, column=1, pady=5)


#REGISTER PAGE
Label(RegisterPage, text='', bg='green', width=30).grid(row=0, column=0, pady=50)
Label(RegisterPage, text='REGISTER', width=40).grid(row=0, column=1, pady=5)
Label(RegisterPage, text='', bg='red', width=30).grid(row=0, column=2, pady=50)

Label(RegisterPage, text='', bg='green', width=30).grid(row=1, column=0, pady=5)
Label(RegisterPage, text="Enter username").grid(row=1, column=1, pady=2)
username = StringVar()
Label(RegisterPage, text='', bg='green', width=30).grid(row=1, column=0, pady=5)
Entry(RegisterPage, textvariable=username).grid(row=2, column=1, pady=2)
Label(RegisterPage, text="Password").grid(row=3, column=1, pady=2)
psswd = StringVar()
Entry(RegisterPage, show="*", textvariable=psswd).grid(row=4, column=1, pady=2)
Label(RegisterPage, text="Confirm password").grid(row=5, column=1, pady=2)
confirm = StringVar()
Label(RegisterPage, text='', width=30).grid(row=1, column=0, pady=5)

Entry(RegisterPage, show="*", textvariable=confirm).grid(row=6, column=1, pady=2)
Button(RegisterPage, text="SUBMIT", command=lambda: check_register_info(username.get(),
                                                                        psswd.get(),
                                                                        confirm.get())).grid(row=7, column=1, pady=5)
Button(RegisterPage, text="Home", command=lambda: raise_frame(HomePage)).grid(row=8, column=1, pady=5)
Button(RegisterPage, text="Login", command=lambda: raise_frame(LoginPage)).grid(row=9, column=1, pady=5)
Button(RegisterPage, text="Quit", command=lambda: quitt_app()).grid(row=10, column=1, pady=5)


#LOGIN PAGE
Label(LoginPage, text='', bg='green', width=30).grid(row=0, column=0, pady=5)

Label(LoginPage, text='LOGIN', width=40).grid(row=0, column=1, pady=5)
Label(LoginPage, text='', bg='red', width=30).grid(row=0, column=2, pady=5)

Label(LoginPage, text="Enter username").grid(row=1, column=1, pady=2)
nameLogin = StringVar()
Entry(LoginPage, textvariable=nameLogin).grid(row=2, column=1, pady=2)
Label(LoginPage, text="Enter password").grid(row=3, column=1, pady=2)
psswdLogin = StringVar()
Entry(LoginPage, show="*", textvariable=psswdLogin).grid(row=4, column=1, pady=2)
Button(LoginPage, text="Submit", command=lambda: check_creds_info(nameLogin.get(), psswdLogin.get())).grid(row=5, column=1, pady=5)
Button(LoginPage, text="Home", command=lambda: raise_frame(HomePage)).grid(row=6, column=1, pady=5)
Button(LoginPage, text="Quit", command=lambda: quitt_app()).grid(row=7, column=1, pady=5)


#CATEGORIES PAGE
Label(CategoryPage, text='', width=25).grid(row=0, column=0, pady=5)

Label(CategoryPage, text='CATEGORIES', bg='grey', width=40).grid(row=0, column=1, pady=5)
Label(CategoryPage, text='', width=25).grid(row=0, column=2, pady=5)

Label(CategoryPage,
      text="Please choose a category by entering the referent number :").grid(row=1, column=1, pady=30)
Entry(CategoryPage, textvariable=psswdLogin, width=4).grid(row=2, column=1, pady=15)
LabelFrame(CategoryPage, text="Catégories", bd=1).grid(padx=10, pady=10)

Button(CategoryPage, text='VALID').grid(row=3, column=1, pady=5)

Label(CategoryPage, text="Boissons sans alcool", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=4, column=0, pady=15)
Label(CategoryPage, text="Boissons alcoolisées", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=4, column=1, pady=15)
Label(CategoryPage, text="Juts de fruits", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=4, column=2, pady=15)

Label(CategoryPage, text="A tartiner", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=5, column=0, pady=15)
Label(CategoryPage, text="Desserts", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=5, column=1, pady=15)
Label(CategoryPage, text="Fruit juices", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=5, column=2, pady=15)

Label(CategoryPage, text="Viandes", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=6, column=0, pady=15)
Label(CategoryPage, text="Biscuits apéritifs", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=6, column=1, pady=15)
Label(CategoryPage, text="Bonbons", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=6, column=2, pady=15)

Button(CategoryPage, text="Home", command=lambda: raise_frame(HomePage)).grid(row=20, column=1,)
Button(CategoryPage, text="Quit", command=lambda: quitt_app()).grid(row=21,
                                                                    column=1)


def check_register_info(username, psswd, confirm):
    if is_valid_register(username, psswd, confirm):
        insert_register_infos(username, psswd)
        messagebox.showinfo("Regestered!", "Your account is created!")
        raise_frame(CategoryPage)


def check_creds_info(username, psswd):
        if is_valid_login(username, psswd):
                messagebox.showinfo('Wellcome','SUCCESS')
                raise_frame(CategoryPage)
        

raise_frame(HomePage)
root.mainloop()