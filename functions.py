import sys
from tkinter import messagebox
from passlib.hash import sha256_crypt
from datetime import datetime
import pymysql


def quitt_app():
    sys.exit()


def is_valid_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def is_valid_register(username, psswd, confirm):
    '''Check entered values by user'''
    if username == "":
            messagebox.showinfo("Register failed", "Empty field!")  
            return False
    else:
        if psswd != confirm:
            messagebox.showinfo("Register failed",
                                "Passwords are not similar: \n Please try again...")
            return False
        elif psswd == "":
            messagebox.showinfo("Register failed", "empty field")
            return False
        else:
            return True


def in_database(username):
    conn , c = connect_to_db()
    c.execute('SELECT * FROM users WHERE user_login LIKE \'%' + username + '%\'')
    result = c.fetchone()
    if result == None:
        return False
        messagebox.showwarning('Faild', 'No user at this name')
    else:
        return True


def connect_to_db():
    conn = pymysql.connect(host="localhost",
                                    user="root",
                                    passwd="Antoine",
                                    db="foodappdb")
    c = conn.cursor()
    return conn, c

def insert_register_infos(username, psswd):
    """Method used to check if registered or not"""
    conn = pymysql.connect(host="localhost",
                           user="root",
                           passwd="Antoine",
                           db="foodappdb")
    c = conn.cursor()
    hashedPsswd = sha256_crypt.encrypt(psswd)
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d')
    sql = 'INSERT INTO users (user_login, user_password, user_date) VALUES (%s,%s,%s)'
    val = ({username}, {hashedPsswd}, {formatted_date})
    c.execute(sql, val)
    conn.commit()
    c.close()


def is_valid_login(username, psswd):
    conn, c = connect_to_db()
    if username != '' and psswd != '':
            c.execute('SELECT * FROM users WHERE user_login LIKE \'%' + username + '%\'')
            result = c.fetchone()
            conn.commit()
            c.close()
            conn.close()
            if result == None:
                messagebox.showinfo('Pas inscrit?','Enreigstrez vous pour utiliser\n          l\'application')
            else:
                check = sha256_crypt.verify(psswd, result[2])
                if check:
                    return True
                else:
                    messagebox.showwarning('Incorrect', 'Mauvais mot de passe')
    else:
        messagebox.showwarning('Attention', 'Tous les champs doivent être remplis')


def display_products_names(products):
    count = 1
    initial_list = []
    for i in products:
        try:
            name = i['product_name_fr']
        except KeyError:
            pass
        if name == '':
            pass
        else:
            initial_list.append(f'{count}:-> {name}\n')  
            count += 1 
            list_to_display = ', '.join(initial_list)
            list_to_display = list_to_display.replace(', ', '')
    return list_to_display



def display_alternative(product):    
  
    try:
        marque = f'Distributeur : {product["brands"]}\n'
    except KeyError:
        marque = 'Distributeur : Information non spécifiée\n'
    try:
        name = f'Nom : {product["name"]}\n'
    except KeyError:
        name = 'Nom :  Information non spécifiée\n'
    try:
        score = f'Nutriscore : {product["brands"]}\n'
    except KeyError:
        score = 'Nutriscore: non précisé'
    url = f'Liens internet : {product["url"]}\n'
    try:        
        alergen = f'Allergène(s) : {product["allergens_from_user"]}\n'
    except KeyError:
        alergen = 'Allergènes : Pas de données disponible\n'
    places = f'Disponible chez : {product["stores"]}\n'
    try:
        otherName = f'Autre appellation : {product["generic_name_fr"]}\n'
    except KeyError:
        otherName = 'Autre appellation: Aucune autre appellation mentionnée\n'
    try:
        complement =f'Composition: {product["ingredients_text"][0:50]}...\n'
    except KeyError:
        complement = 'Compoition: Informations non disponibles'
    try:
        portion = f'Portion : {product["nutrition_data_prepared_per"]}\n'
    except KeyError:
        portion = 'Portion: Information non communiquée'
        
    code = f'Code produit : {product["code"]}\n'
      
    aliment = [name,otherName, marque, places, score, url, alergen , complement, portion, code]
    list_to_display = ', '.join(aliment)
    list_to_display = list_to_display.replace(', ', '')
    return list_to_display


def dump_selection(selection, userSession):    
    check_values(selection)
    conn , c = connect_to_db()
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d')
    sql = 'INSERT INTO products (brands, name, nutriscore, url, alergen, stores, other_name, complement, portion, code, date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    val = ({selection.brands},
           {selection.name},
           {selection.nutriscore},
           {selection.url},
           {selection.alergen},
           {selection.stores},
           {selection.other_name},
           {selection.complement},
           {selection.portion},
           {selection.code},
           {formatted_date})
    c.execute(sql, val)
    conn.commit()
    c.close()
    print('dumped success!')
    return True
    

def check_values(selection):
    try:
        selection.other_name
    except AttributeError:
        selection.other_name = 'Non communiqué'
    try:
        selection.complement
    except AttributeError:
        selection.complement = 'Non communiqué'
    try:
        selection.portion
    except AttributeError:
        selection.portion = 'Non communiqué'