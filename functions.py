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
                                "Passwords are not \
                                 similar: \n Please try again...")
            return False
        elif psswd == "":
            messagebox.showinfo("Register failed", "empty field")
            return False
        else:
            return True


def in_database(username):
    conn, c = connect_to_db()
    c.execute('SELECT * FROM users WHERE login LIKE \'%' + username + '%\'')
    result = c.fetchone()
    if result is None:
        return False
        messagebox.showwarning('Faild', 'No user at this name')
    else:
        return True


def connect_to_db():
    conn = pymysql.connect(host="localhost",
                           user="user_foodapp",
                           passwd="p@ssword",
                           db="foodappdb")
    c = conn.cursor()
    return conn, c


def insert_register_infos(username, psswd):
    """Method used to check if registered or not"""
    conn, c = connect_to_db()
    hashedPsswd = sha256_crypt.encrypt(psswd)
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d')
    sql = 'INSERT INTO users (login, psswd, date) VALUES (%s,%s,%s)'
    val = ({username}, {hashedPsswd}, {formatted_date})
    c.execute(sql, val)
    conn.commit()
    c.close()


def is_valid_login(username, psswd):
    conn, c = connect_to_db()
    if username != '' and psswd != '':
            c.execute('SELECT * \
                       FROM users \
                       WHERE login LIKE \'%' + username + '%\'')
            result = c.fetchone()
            conn.commit()
            c.close()
            conn.close()
            if result is None:
                messagebox.showinfo('Pas inscrit?',
                                    'Enreigstrez vous pour \
                                     utiliser\n          l\'application')
            else:
                check = sha256_crypt.verify(psswd, result[2])
                if check:
                    return True
                else:
                    messagebox.showwarning('Incorrect', 'Mauvais mot de passe')
    else:
        messagebox.showwarning('Attention', 'Tous les champs \
                                doivent être remplis')


def display_products_names(products):
    count = 1
    initial_list = []
    for i in products:
        try:
            name = i['product_name_fr']
        except:
            name = 'Non communiqué'
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
    except:
        marque = 'Distributeur : Information non spécifiée\n'
    try:
        name = f'Nom : {product["product_name"]}\n'
    except:
        name = 'Nom :  Information non spécifiée\n'
    try:
        score = f'Nutriscore : {product["nutrition_grades"]}\n'
    except:
        score = 'Nutriscore: non précisé\n'
    try:
        url = f'Liens internet : {product["url"]}\n'
    except:
        url = f'Information non communiquée'
    try:        
        alergen = f'Allergène(s) : {product["allergens_from_ingredients"]}\n'
    except:
        alergen = 'Allergènes : Pas de données disponible\n'
    try:
        places = f'Magasins : {product["stores"]}\n'
    except:
        places = f'Magasin : Pas de magasin spécifié'
    try:
        otherName = f'Autre appellation : {product["generic_name_fr"]}\n'
    except:
        otherName = 'Autre appellation: Aucune autre appellation mentionnée\n'
    try:
        complement = f'Composition: {product["ingredients_text"][0:50]}...\n'
    except:
        complement = 'Composition: Informations non disponibles\n'
    try:
        portion = f'Portion : {product["nutrition_data_prepared_per"]}\n'
    except:
        portion = 'Portion: Information non communiquée'
    try:   
        code = f'Code produit : {product["code"]}\n'
    except:
        code = 'Code non disponible'

    aliment = [name, otherName, marque, places, score, url,
               alergen, complement, portion, code]
    list_to_display = ', '.join(aliment)
    list_to_display = list_to_display.replace(', ', '')
    return list_to_display


def dump_selection(selection, userSession):
    if not in_db(selection):
        if in_favorites(selection):
            messagebox.showinfo('Produit deja favori',
                                "Ce produit figure déjà dans vos favoris")
        else:
            insert_product(selection)
            insert_favorites(selection, userSession)
    else:
        messagebox.showwarning('Deja dans la base',
                               "Information deja dans la base de donnees")


def insert_product(selection):
    conn, c = connect_to_db()
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d')

    sql = 'INSERT INTO products (brands, name, nutriscore, url,\
           alergen, stores, other_name, complement, portion, code, date)\
           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
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
    return True


def check_values(selection, userSession):
    userId = get_user_id(userSession.login)
    productId = get_product_id(selection.code)


def insert_favorites(selection, userSession):
    conn, c = connect_to_db()
    c.execute('SELECT id \
               FROM products\
               WHERE code \
               LIKE \'%' + selection.code + '%\'')
    productId = c.fetchone()
    c.execute('SELECT id \
               FROM users \
               WHERE login \
               LIKE \'%' + userSession.login + '%\'')
    userId = c.fetchone()
    sql = 'INSERT INTO favorites (users_id, products_id) VALUES (%s,%s)'
    val = ({userId}, {productId})
    c.execute(sql, val)
    conn.commit()
    c.close()
    messagebox.showinfo('Enregistré!', "Votre produit a été enregistré")


def in_favorites(selection):
    conn, c = connect_to_db()
    c.execute('SELECT id FROM products \
               WHERE code \
               LIKE \'%' + selection.code + '%\'')
    productId = c.fetchone()
    if productId:
        c.execute('SELECT * \
                   FROM favorites \
                   WHERE product_id LIKE \'%' + productId + '%\'')
        favoritId = c.fetchone()
        if favoritId:
            if productId == favoritId:
                return False
            else:
                return True
    else:
        return False
    conn.commit()
    c.close()
    conn.close()


def get_user_id(login):
    conn, c = connect_to_db()
    c.execute('SELECT id \
               FROM users \
               WHERE login \
               LIKE \'%' + login + '%\'')
    userId = c.fetchone()
    conn.commit()
    c.close()
    conn.close()
    return userId


def in_db(selection):
    conn, c = connect_to_db()
    c.execute('SELECT id \
               FROM products \
               WHERE code \
               LIKE \'%' + selection.code + '%\'')
    productId = c.fetchone()
    if productId:
        return True
    else:
        return False
    conn.commit()
    c.close()
    conn.close()


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


def set_default(new):
    print(f"TYPE DE NEW {type(new)}")
    try:
        new["brands"]
    except:
        new["brands"] = 'Distributeur : Information non spécifiée\n'
    try:
        new["name"]
    except:
        new["name"] = 'Nom :  Information non spécifiée\n'
    try:
        new["score"]
    except:
        score = 'Nutriscore: non précisé'
    try:
        new["allergens_from_user"]
    except:
        new["allergens_from_user"] = 'Allergènes : Pas de données disponible\n'
    try:
        new["stores"]
    except:
        places = new["stores"]
    try:
        new["generic_name_fr"]
    except:
        otherName = "Pas d'information supplémentaire"
    try:
        new["ingredients_text"]
    except:
        new["ingredients_text"] = 'Compoition: Informations non disponibles'
    try:
        new["nutrition_data_prepared_per"]
    except:
        new["nutrition_data_prepared_per"] = \
            'Portion: Information non communiquée'
    return new


def request_saved(user, id):
    id = id[0]
    i = str(id)
    conn, c = connect_to_db()
    c.execute(f'SELECT P.* \
                FROM products \
                AS P \
                LEFT JOIN favorites AS F \
                ON F.products_id = P.id WHERE F.users_id = {id} ;')
    saved = c.fetchall()
    conn.commit()
    c.close()
    conn.close()
    return saved


def display_history(saved):
    elements = []
    for i in saved:
        elements.append(f'Nom : {i[2]}\n')
        elements.append(f'Nutriscore : {i[3]}\n')
        elements.append(f'URL : {i[4]}\n')
        elements.append(f'Magasin : {i[7]}\n')
        elements.append('----------------------------------------\n')
    toDisplay = ', '.join(elements)
    toDisplay = toDisplay.replace(', ', '')
    return toDisplay