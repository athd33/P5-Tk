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


def in_database(username):
    conn = pymysql.connect(host="localhost",
                                    user="root",
                                    passwd="Antoine",
                                    db="foodappdb")
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE user_login LIKE \'%' + username + '%\'')
    result = c.fetchone()
    if result == None:
        return False
        messagebox.showwarning('Faild', 'No user at this name')
    else:
        return True


def is_valid_login(username, psswd):
    if username != '' and psswd != '':
            conn = pymysql.connect(host="localhost",
                                    user="root",
                                    passwd="Antoine",
                                    db="foodappdb")
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE user_login LIKE \'%' + username + '%\'')
            result = c.fetchone()
            conn.commit()
            c.close()
            conn.close()
            if result == None:
                messagebox.showinfo('No account yet?','Please register')
            else:
                check = sha256_crypt.verify(psswd, result[2])
                if check == True:
                    return True
                else:
                    messagebox.showwarning('Invalid', 'Wrong password, try again..')
    else:
        messagebox.showwarning('Invalid', 'Watch out! Empty field??')


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
    
    
def is_valid_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False