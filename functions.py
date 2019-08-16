import sys
from tkinter import messagebox
from passlib.hash import sha256_crypt
import pymysql

def quitt_app():
    sys.exit()


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

def insert_register_infos(username, psswd):
    """Method used to check if registered or not"""
    conn = pymysql.connect(host="localhost",
                           user="root",
                           passwd="Antoine",
                           db="foodappdb")
    c = conn.cursor()
    hashedPsswd = sha256_crypt.encrypt(psswd)
    sql = 'INSERT INTO users (user_login, user_password) VALUES (%s,%s)'
    val = ({username}, {hashedPsswd})
    c.execute(sql, val)
    conn.commit()
    c.close()
    messagebox.showinfo('Registered!', 'Registered OK!\nWellcome!')
    
