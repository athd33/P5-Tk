import sys
from tkinter import messagebox
from passlib.hash import sha256_crypt
from datetime import datetime
import pymysql


def quitt_app():
    sys.exit()


def is_valid_register(username, psswd, confirm):
    '''Check entered values by user'''
    if username == "":
            messagebox.showinfo("Register failed", "Empty field!")  
            return False
    elif in_database(username):
            messagebox.showinfo("Register failed", "Username allready taken:\nChoose an other please")
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


def connect_to_db():
    conn = pymysql.connect(host="localhost",
                                    user="root",
                                    passwd="Antoine",
                                    db="foodappdb")
    c = conn.cursor()
    return conn, c


def in_database(username):
    conn , c = connect_to_db()
    c.execute('SELECT * FROM users WHERE user_login LIKE \'%' + username + '%\'')
    result = c.fetchone()
    if result == None:
        return False
        messagebox.showwarning('Faild', 'No user at this name')
    else:
        return True


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
    
    
def is_valid_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

#def get_aliment_list(num):