import requests
from appclasses import AlternativeProduct
from tkinter import messagebox
from random import *


def get_aliment_liste(num):
    num -= 1
    aliments = ['pizza', 'yaourt', 'boisson', 'vin', 'dessert']
    req = requests.get(f'https://world.openfoodfacts.org/cgi/search.pl?search_terms={aliments[num]}&page_size=20&process&json=1')
    responseCode = req.status_code
    if responseCode != 200:
        print(f'Error in request, returned code :{responseCode}')
    else:
        result = req.json()
        products = result["products"]        
        return products
        

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
    selectedProduct = AlternativeProduct(product)   # instanciation de selectedProduct
    marque = 'Marque : -------------\n'
    name = 'Nom : -------------\n'
    otherName = 'Information indisponible\n'
    score = 'Information indisponible\n'
    url = 'Plus d\'informations sur : https://fr.openfoodfacts.org/decouvrir\n'
    alergen = 'Allergène(s) : -------------\n'
    places = 'Lieux de ventes : -------------\n'
    complement = 'Composition : ----------------\n'
    portion = 'Portion : ----------\n'
    code = 'Code produit : -----------\n'
    country = 'Pays de fabrication : ---------\n'
    try:
        marque = f'Distributeur : {product["brands"]}\n'
        name = f'Nom : {product["product_name_fr"]}\n'
        score = f'Nutriscore : {product["nutrition_grades"]}\n'
        url = f'Liens internet : {product["url"]}\n'
        alergen = f'Allergène(s) : {product["allergens_from_ingredients"]}\n'
        places = f'Disponible chez : {product["stores"]}\n'
        otherName = f'Autre appellation : {product["product_name"]}\n'
        complement =f'Composition: {product["ingredients_text"][0:100]}...\n'
        portion = f'Portion : {product["nutrition_data_prepared_per"]}\n'
        code = f'Code produit : {product["code"]}\n'
        country = f'Code produit : {product["country"]}\n'
    except KeyError:
        pass        
    aliment = [name,otherName, marque, places, score, url, alergen , complement, portion, country, code]
    list_to_display = ', '.join(aliment)
    list_to_display = list_to_display.replace(', ', '')
    return list_to_display




def select_alternative(product):
    cat = product['categories']
    req = requests.get(f'https://world.openfoodfacts.org/cgi/search.pl?search_terms={cat}&nutrition_grades=a&countries_lc=fr&page_size=20&process&json=1')
    responseCode = req.status_code
    if responseCode != 200:
        print(f'Error in request, returned code :{responseCode}')
    else:
        try:
            result = req.json()
            products = result["products"]
            num  = len(products)
            rNum = randrange(num)
            new = products[rNum]            
            return display_alternative(new)
        except ValueError:            
            try:                
                new = try_request(cat, "b")                          
                return display_alternative(new)
            except ValueError:
                new = try_request(cat,"c")                          
                return display_alternative(new)
            except ValueError:
                messagebox.showinfo("'Arf!', 'Arf, pas d'alternative en stock.\nCherchez un autre produit?'")


def try_request(cat, letter):
    req = requests.get(f'https://world.openfoodfacts.org/cgi/search.pl?search_terms={cat}&nutrition_grades={letter}&countries_lc=fr&page_size=20&process&json=1')
    result = req.json()
    products = result["products"]
    num  = len(products)                                  
    rNum = randrange(num)
    new = products[rNum]                            
    return new