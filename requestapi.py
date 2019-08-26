import requests
from appclasses import Product
from tkinter import messagebox
from random import *


def get_aliment_list(num):
    num -= 1
    aliments = ['pizza', 'yaourts', 'burger', 'desserts', 'snacks', 'cakes', 'apéritifs', 'sandwich', 'pain']
    choice = aliments[num]
    req = requests.get(f'https://world.openfoodfacts.org/cgi/search.pl?search_terms={choice}&page_size=20&process&json=1')
    responseCode = req.status_code
    if responseCode != 200:
        print(f'Error in request, returned code :{responseCode}')
    else:
        result = req.json()
        products = result["products"]
        return products, choice


def select_alternative(choice):
    print(f'PREMIER CHOICE : {choice}')
    req = requests.get(f'https://world.openfoodfacts.org/cgi/search.pl?search_terms={choice}&nutrition_grades=a&page_size=20&process&json=1')
    responseCode = req.status_code
    if responseCode != 200:
        print(f'Error in request, returned code :{responseCode}')
    else:
        result = req.json()
        products = result["products"]
        num = len(products)
        if num == 0:
            products = try_request(choice, 'b')
            if num == 0:
                products = try_request(choice, 'c')
                if num == 0:
                    products = try_request(choice, 'd')
                    if num == 0:
                        messagebox.showinfo('Arf', 'Nous ne trouvons pas d\'alternative,\n essayez avec un autre produit!')
                        return False
                else:
                    rNum = randrange(num)
                    new = products[rNum]
                    return new
            else:
                rNum = randrange(num)
                new = products[rNum]
                return new
        else:
            rNum = randrange(num)
            new = products[rNum]
            return new


def try_request(choice, letter):
    req = requests.get(f'https://world.openfoodfacts.org/cgi/search.pl?search_terms={choice}&nutrition_grades={letter}&page_size=20&process&json=1')
    result = req.json()
    products = result["products"]
    num = len(products)
    if num == 0:
        return num, choice
    else:
        return products
