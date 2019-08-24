import requests
from appclasses import Product
from tkinter import messagebox
from random import *


def get_aliment_list(num):
    num -= 1
    aliments = ['pizzas', 'yaourts', 'boissons', 'desserts', 'snacks', 'cakes', 'apéritifs', '', '']
    req = requests.get(f'https://world.openfoodfacts.org/cgi/search.pl?search_terms={aliments[num]}&page_size=20&process&json=1')
    responseCode = req.status_code
    if responseCode != 200:
        print(f'Error in request, returned code :{responseCode}')
    else:
        result = req.json()
        products = result["products"]        
        return products
        
def select_alternative(product):
    cat = product['categories']
    req = requests.get(f'https://world.openfoodfacts.org/cgi/search.pl?search_terms={cat}&nutrition_grades=a&countries_lc=fr&page_size=20&process&json=1')
    responseCode = req.status_code
    if responseCode != 200:
        print(f'Error in request, returned code :{responseCode}')
    else:
        result = req.json()
        products = result["products"]
        num  = len(products)   
        print(f'nombre de resultat a : {num}')
        if num == 0:
            products = try_request(cat, 'b')
            num = len(products)
            print(f'nombre de resultat b : {num}')
            if num == 0:
                products = try_request(cat, 'c')
                num = len(products)
                print(f'nombre de resultat c : {num}')
                if num == 0:
                    products = try_request(cat, 'd')
                    num = int(num)                
                    num = len(products)
                    print(f'nombre de resultat d : {num}')
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


def try_request(cat, letter):       
    req = requests.get(f'https://world.openfoodfacts.org/cgi/search.pl?search_terms={cat}&nutrition_grades={letter}&countries_lc=fr&page_size=20&process&json=1')
    result = req.json()
    products = result["products"]
    num  = len(products)  
    if num == 0:
        return num
    else:         
        return products