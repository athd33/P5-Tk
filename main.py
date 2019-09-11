from tkinter import messagebox, Tk, Frame, Label, Button, Entry
from tkinter import StringVar, LabelFrame, Text, PhotoImage, IntVar
from appclasses import User, Product
from functions import quitt_app, is_valid_register, in_database, get_user_id
from functions import insert_register_infos, is_valid_login, display_history
from functions import is_valid_number, display_alternative, dump_selection
from functions import set_default, request_saved, display_products_names
from requestapi import get_aliment_list, select_alternative
import requests
import sys


root = Tk()  # main window
root.title("** P5 -- FOOD SEARCH APP -- ** ")
root.geometry("800x600+300+200")
root.resizable(False, False)
HomePage = Frame(root)  # frames
LoginPage = Frame(root)
RegisterPage = Frame(root)
CategoryPage = Frame(root)
AlimentsPage = Frame(root)
AlternativePage = Frame(root)
HistoryPage = Frame(root)
products = []
num = 0
pro = []


def raise_frame(frame):
    frame.tkraise()

for frame in(HomePage, LoginPage, RegisterPage,
             CategoryPage, AlimentsPage, AlternativePage, HistoryPage):
    frame.grid(row=0, column=0, sticky='news')

# HOME PAGE
Label(HomePage, text='', bg='green', width=30).grid(row=0, column=0, pady=4)
Label(HomePage, text='Accueil', width=40).grid(row=0, column=1, pady=4)
Label(HomePage, text='', bg='red', width=30).grid(row=0, column=2, pady=4)
Button(HomePage, text="Créer un compte", command=lambda: raise_frame(RegisterPage)).grid(row=1, column=1, pady=5)
Button(HomePage, text="M'authentifier", command=lambda: raise_frame(LoginPage)).grid(row=2, column=1, pady=5)
Button(HomePage, text="Quitter", command=lambda: quitt_app()).grid(row=3, column=1, pady=5)


#REGISTER PAGE
Label(RegisterPage, text='', bg='green', width=30).grid(row=0, column=0, pady=5)
Label(RegisterPage, text='AUTHENTIFICATION', width=40).grid(row=0, column=1, pady=5)
Label(RegisterPage, text='', bg='red', width=30).grid(row=0, column=2, pady=5)
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
Button(RegisterPage, text="SUBMIT",
       command=lambda: check_register_info(username.get(), psswd.get(), confirm.get())).grid(row=7, column=1, pady=5)
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
Label(CategoryPage, text='', width=30, bg='green').grid(row=0, column=0, pady=5)
Label(CategoryPage, text='    CATEGORIES  ', width=40).grid(row=0, column=1, pady=5)
Label(CategoryPage, text='', width=30, bg='red').grid(row=0, column=2, pady=5)
Label(CategoryPage,
      text="Quel aliment souhaitez-vous remplacer ? :").grid(row=1, column=1, pady=30)
choiceNumber = StringVar()
Entry(CategoryPage, textvariable=choiceNumber, width=4).grid(row=2, column=1, pady=15)
LabelFrame(CategoryPage, text="Catégories", bd=1).grid(padx=10, pady=10)
Button(CategoryPage, text='VALIDER', command=lambda: get_first_list(choiceNumber.get())).grid(row=3, column=1, pady=5)
Label(CategoryPage, text="   1\n  PIZZAS", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=4, column=0, pady=15)
Label(CategoryPage, text="   2\n    YAOURTS", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=4, column=1, pady=15)
Label(CategoryPage, text="    3\n    BURGERS", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=4, column=2, pady=15)
Label(CategoryPage, text="    4\n    DESSERTS", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=5, column=0, pady=15)
Label(CategoryPage, text="   5\nSNACKS", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=5, column=1, pady=15)
Label(CategoryPage, text="    6\nCAKES", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=5, column=2, pady=15)
Label(CategoryPage, text="   7\nAPERITIFS", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=6, column=0, pady=15)
Label(CategoryPage, text="  8\nSANDWICHS", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=6, column=1, pady=15)
Label(CategoryPage, text="    9\nPAINS", borderwidth=2,
      relief="groove", width=20, height=2).grid(row=6, column=2, pady=15)

Button(CategoryPage, text="Accueil", command=lambda: raise_frame(HomePage)).grid(row=20, column=1,)
Button(CategoryPage, text="Quitter", command=lambda: quitt_app()).grid(row=21, column=1)
Button(CategoryPage, text="Retrouver mes\n aliments substitués", command=lambda: get_saved(user), bg='#3F7FBF').grid(row=22, column=1, pady=5)


# ALIMENTS PAGE
Label(AlimentsPage, text='', width=30, bg='green').grid(row=0, column=0, pady=5)
Label(AlimentsPage, text='ALIMENTS', width=30).grid(row=0, column=1, pady=5)
Label(AlimentsPage, text='', width=35, bg='red').grid(row=0, column=2, pady=5)
Label(AlimentsPage, text='Veuillez sélectionner un \naliment dans la liste suivante:').grid(row=1, column=1)
alimentList = StringVar()
Label(AlimentsPage, width=65, height=20, bg="#808080",borderwidth=2, relief="groove", 
      textvariable=alimentList, anchor="nw", justify="left").grid(row=2, column=0, columnspan=3)
alimentNumber = StringVar()
Entry(AlimentsPage,  width=2, bg="#808080",borderwidth=2, textvariable=alimentNumber, relief="groove" ).grid(row=3, column=1, pady=3)
Button(AlimentsPage, text="Valider", command=lambda: get_alternative(alimentNumber.get(), categoryList)).grid(row=4, column=1, pady=3)
Button(AlimentsPage, text="Retour", command=lambda: raise_frame(CategoryPage)).grid(row=5, column=0, pady=2)
Button(AlimentsPage, text="Accueil", command=lambda: raise_frame(HomePage)).grid(row=5, column=2, pady=2)
Button(AlimentsPage, text="Quitter", command=lambda: quitt_app()).grid(row=6, column=1, pady=2)


# ALTERNATIVE PAGE
Label(AlternativePage, text='', width=30, bg='green').grid(row=0, column=0, pady=5)
Label(AlternativePage, text='ALTERNATIVE', width=30).grid(row=0, column=1, pady=5)
Label(AlternativePage, text='', width=35, bg='red').grid(row=0, column=2, pady=5)
Label(AlternativePage, text='Voici une alternative \n   qui\
                             pourrait vous intéresser:').grid(row=1, column=1)
alternativeAliment = StringVar()
Label(AlternativePage, width=90, height=20, bg="#F0F2F4",borderwidth=2, relief="groove", 
      textvariable=alternativeAliment, anchor="nw", justify="left").grid(row=2, column=0, columnspan=3)
Button(AlternativePage, text="Enregistrer", command=lambda:dump_product(product, user)).grid(row=3, column=1, pady=3)
Button(AlternativePage, text="Retour", command=lambda: raise_frame(CategoryPage)).grid(row=4, column=1, pady=2)
Button(AlternativePage, text="Accueil", command=lambda: raise_frame(CategoryPage)).grid(row=5, column=1, pady=2)
Button(AlternativePage, text="Quitter", command=lambda: quitt_app()).grid(row=6, column=1, pady=2)


# HISTORIQUE PAGE
Label(HistoryPage, text='', width=30, bg='green').grid(row=0, column=0, pady=5)
Label(HistoryPage, text='RECHERCHES SAUVEGARDEES', width=40).grid(row=0, column=1, pady=5)
Label(HistoryPage, text='', width=30, bg='red').grid(row=0, column=2, pady=5)
Label(HistoryPage, text='Voici les recherches enregistrées:').grid(row=1, column=1)
savedElements = StringVar()
Label(HistoryPage, width=90, height=20, bg="#808080",borderwidth=2, relief="groove", 
      textvariable=savedElements, anchor="nw", justify="left").grid(row=2, column=0, columnspan=3)
Button(HistoryPage, text="Catégories", command=lambda: raise_frame(CategoryPage)).grid(row=5, column=1, pady=2)
Button(HistoryPage, text="Aliments", command=lambda: raise_frame(AlimentsPage)).grid(row=6, column=1, pady=2)
Button(HistoryPage, text="Quitter", command=lambda: quitt_app()).grid(row=7, column=1, pady=2)


def check_register_info(username, psswd, confirm):
    if is_valid_register(username, psswd, confirm):
        if in_database(username):
            messagebox.showinfo("Register failed",
                                "Username allready taken:\nChoose\
                                 an other please")
        else:
            insert_register_infos(username, psswd)
            global user
            user = User(username, psswd)  # instance User object
            messagebox.showinfo("VALIDE!",
                                f"{username}, votre compte est créé!")
            raise_frame(CategoryPage)


def check_creds_info(username, psswd):
    if is_valid_login(username, psswd):
            messagebox.showinfo('Informations valides',
                                f'Bienvenue  {username}   ')
            global user
            user = User(username, psswd)  # instance User object
            raise_frame(CategoryPage)


def get_first_list(number):
    try:
        number = int(number)
        if number < 1 and number > 9:
            messagebox.showwarning('Erreur de saisie',
                                   'Désolé, il faut un chiffre entre:\n \
                                    1 et 9')
        else:
            global categoryList
            global choice
            categoryList, choice = get_aliment_list(number)
            raise_frame(AlimentsPage)
            alimentList.set(display_products_names(categoryList))
    except:
        messagebox.showwarning('Erreur de saisie', 'Désolé,\
                                il faut un chiffre entre:\n     1 et 9')


def get_alternative(number, products):
    if is_valid_number(number):
        number = int(number)
        if number > 0 and number < 21:
            number -= 1
            raise_frame(AlternativePage)
            new = select_alternative(choice)
            if not new:
                raise_frame(CategoryPage)
            global product
            product = Product(new)
            alternativeAliment.set(display_alternative(new))
        else:
            messagebox.showwarning('Attention',
                                   'Désolé, vous devez choisir dans la liste.')
    else:
        messagebox.showwarning('Erreur de saisie',
                               'Désolé, il faut renseigner un chiffre.')


def dump_product(product, user):
    if dump_selection(product, user):
        messagebox.showinfo('Saved!', 'Your data have been saved')


def get_saved(user):
    raise_frame(HistoryPage)
    id = get_user_id(user.login)
    savedProducts = request_saved(user, id)
    history = display_history(savedProducts)
    savedElements.set(history)


raise_frame(HomePage)
root.mainloop()