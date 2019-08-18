from tkinter import messagebox, Tk, Frame, Label, Button, Entry, StringVar, LabelFrame, Text
from appclasses import User
import requests
from functions import quitt_app, is_valid_register, insert_register_infos, is_valid_login, is_valid_number
import sys 


root=Tk() # main window
root.title("** P5 -- FOOD SEARCH APP -- ")
root.geometry("800x600+300+200")

HomePage = Frame(root)  # frames
LoginPage = Frame(root)
RegisterPage = Frame(root)
CategoryPage = Frame(root)
AlimentsPage = Frame(root)

def raise_frame(frame):
    frame.tkraise()


for frame in(HomePage, LoginPage, RegisterPage, CategoryPage, AlimentsPage):
    frame.grid(row=0, column=0, sticky='news')

# HOME PAGE
Label(HomePage, text='', bg='green', width=30).grid(row=0, column=0, pady=4)
Label(HomePage, text='Accueil', width=40).grid(row=0, column=1, pady=4)
Label(HomePage, text='', bg='red', width=30).grid(row=0, column=2, pady=4)

Button(HomePage, text="Créer un compte", command=lambda: raise_frame(RegisterPage)).grid(row=1, column=1, pady=5)
Button(HomePage, text="M'authentifier", command=lambda: raise_frame(LoginPage)).grid(row=2, column=1, pady=5)
Button(HomePage, text="Quitter", command=lambda: quitt_app()).grid(row=3, column=1, pady=5)


#REGISTER PAGE
Label(RegisterPage, text='', bg='green', width=30).grid(row=0, column=0, pady=50)
Label(RegisterPage, text='AUTHENTIFICATION', width=40).grid(row=0, column=1, pady=5)
Label(RegisterPage, text='', bg='red', width=30).grid(row=0, column=2, pady=50)

Label(RegisterPage, text='', bg='green', width=30).grid(row=1, column=0, pady=5)
Label(RegisterPage, text="Nom d'utilisateur").grid(row=1, column=1, pady=2)
username = StringVar()
Label(RegisterPage, text='', bg='green', width=30).grid(row=1, column=0, pady=5)
Entry(RegisterPage, textvariable=username).grid(row=2, column=1, pady=2)
Label(RegisterPage, text="Mot de passe").grid(row=3, column=1, pady=2)
psswd = StringVar()
Entry(RegisterPage, show="*", textvariable=psswd).grid(row=4, column=1, pady=2)
Label(RegisterPage, text="Confirmez le mot de passe").grid(row=5, column=1, pady=2)
confirm = StringVar()
Label(RegisterPage, text='', width=30).grid(row=1, column=0, pady=5)

Entry(RegisterPage, show="*", textvariable=confirm).grid(row=6, column=1, pady=2)
Button(RegisterPage, text="SUBMIT", command=lambda: check_register_info(username.get(),
                                                                        psswd.get(),
                                                                        confirm.get())).grid(row=7, column=1, pady=5)
Button(RegisterPage, text="Accueil", command=lambda: raise_frame(HomePage)).grid(row=8, column=1, pady=5)
Button(RegisterPage, text="Authentification", command=lambda: raise_frame(LoginPage)).grid(row=9, column=1, pady=5)
Button(RegisterPage, text="Quitter", command=lambda: quitt_app()).grid(row=10, column=1, pady=5)


#LOGIN PAGE
Label(LoginPage, text='', bg='green', width=30).grid(row=0, column=0, pady=5)

Label(LoginPage, text='AUTHENTIFICATION', width=40).grid(row=0, column=1, pady=5)
Label(LoginPage, text='', bg='red', width=30).grid(row=0, column=2, pady=5)

Label(LoginPage, text="Votre nom d'utilisateur").grid(row=1, column=1, pady=2)
nameLogin = StringVar()
Entry(LoginPage, textvariable=nameLogin).grid(row=2, column=1, pady=2)
Label(LoginPage, text="Mot de passe").grid(row=3, column=1, pady=2)
psswdLogin = StringVar()
Entry(LoginPage, show="*", textvariable=psswdLogin).grid(row=4, column=1, pady=2)
Button(LoginPage, text="Valider", command=lambda: check_creds_info(nameLogin.get(), psswdLogin.get())).grid(row=5, column=1, pady=5)
Button(LoginPage, text="Accueil", command=lambda: raise_frame(HomePage)).grid(row=6, column=1, pady=5)
Button(LoginPage, text="Quitter", command=lambda: quitt_app()).grid(row=7, column=1, pady=5)


#CATEGORIES PAGE
Label(CategoryPage, text='', width=25, bg='green').grid(row=0, column=0, pady=5)

Label(CategoryPage, text='    CATEGORIES  ', width=40).grid(row=0, column=1, pady=5)
Label(CategoryPage, text='', width=25, bg='red').grid(row=0, column=2, pady=5)

Label(CategoryPage,
      text="Choisissez une catégorie parmi les propositions suivantes :").grid(row=1, column=1, pady=30)

choiceNumber = StringVar()
Entry(CategoryPage, textvariable=choiceNumber, width=4).grid(row=2, column=1, pady=15)
LabelFrame(CategoryPage, text="Catégories", bd=1).grid(padx=10, pady=10)

Button(CategoryPage, text='VALIDER', command=lambda: [raise_frame(AlimentsPage),
                                                      get_test()]).grid(row=3, column=1, pady=5)

Label(CategoryPage, text="   1\n  PIZZAS", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=4, column=0, pady=15)
Label(CategoryPage, text="   2\n    YAOURT", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=4, column=1, pady=15)
Label(CategoryPage, text="    3\n    BISCUITS", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=4, column=2, pady=15)

Label(CategoryPage, text="    4\n    PATES", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=5, column=0, pady=15)
Label(CategoryPage, text="   5\nDesserts", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=5, column=1, pady=15)
Label(CategoryPage, text="    6\nFruit juices", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=5, column=2, pady=15)

Label(CategoryPage, text="   7\nViandes", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=6, column=0, pady=15)
Label(CategoryPage, text="  8\nBiscuits apéritifs", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=6, column=1, pady=15)
Label(CategoryPage, text="    9\nBonbons", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=6, column=2, pady=15)

Button(CategoryPage, text="Accueil", command=lambda: raise_frame(HomePage)).grid(row=20, column=1,)
Button(CategoryPage, text="Quitter", command=lambda: quitt_app()).grid(row=21,
                                                                    column=1)




# ALIMENTS PAGE
Label(AlimentsPage, text='', width=35, bg='green').grid(row=0, column=0, pady=5)

Label(AlimentsPage, text='ALIMENTS', width=30).grid(row=0, column=1, pady=5)
Label(AlimentsPage, text='', width=35, bg='red').grid(row=0, column=2, pady=5)

Label(AlimentsPage, text='Veuillez sélectionner un \naliment dans la liste suivante:').grid(row=1, column=0)

aliments = StringVar()
Label(AlimentsPage, width=20, height=20, textvariable=aliments, bg="white", anchor="nw").grid(row=1, column=1)

Button(AlimentsPage, text="Catégories", command=lambda: raise_frame(CategoryPage)).grid(row=2, column=0, pady=2)
Button(AlimentsPage, text="Rechercher", command=lambda: raise_frame(CategoryPage)).grid(row=2, column=2, pady=2)

Button(AlimentsPage, text="Accueil", command=lambda: raise_frame(HomePage)).grid(row=2, column=1, pady=2)
Button(AlimentsPage, text="Quitter", command=lambda: quitt_app()).grid(row=21, column=1, pady=2)





def check_register_info(username, psswd, confirm):
    if is_valid_register(username, psswd, confirm):
        insert_register_infos(username, psswd)
        messagebox.showinfo("VALIDE!", "Votre compte est créé!")
        raise_frame(CategoryPage)


def check_creds_info(username, psswd):
        if is_valid_login(username, psswd):
                messagebox.showinfo('Informations valides', 'Bienvenue')
                userSession = User(username, psswd)  # instance User object
                raise_frame(CategoryPage)
        

def check_number(number):
        if is_valid_number(number):
                print("OK")
        else:
                messagebox.showwarning('Erreur', '       Attention:\n il faut entrer un chiffre')










raise_frame(HomePage)
root.mainloop()