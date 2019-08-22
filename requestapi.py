import requests
from appclasses import AlternativeProduct
from tkinter import messagebox
from random import *


def get_aliment_liste(num):
    num -= 1
    aliments = ['pizzas', 'yaourts', 'boissons', 'desserts', 'dessert', 'bières', 'apéritifs', '', '']
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
    
    marque = f'Distributeur : {selectedProduct.brands}\n'
    name = f'Nom : {selectedProduct.name}\n'
    score = f'Nutriscore : {selectedProduct.nutriscore}\n'
    url = f'Liens internet : {selectedProduct.url}\n'
    alergen = f'Allergène(s) : {selectedProduct.alergen}\n'
    places = f'Disponible chez : {selectedProduct.stores}\n'
    otherName = f'Autre appellation : {selectedProduct.productsName}\n'
    complement =f'Composition: {product["ingredients_text"][0:50]}...\n'
    portion = f'Portion : {product["nutrition_data_prepared_per"]}\n'
    code = f'Code produit : {product["code"]}\n'
      
    aliment = [name,otherName, marque, places, score, url, alergen , complement, portion, code]
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
            print(f'NOMBRE DE RESULTATS {num}')
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
    if num > 0:
        print(f'NOMBRE DE RESULTATS ALTERNATIF {letter} -- > {num}')                               
        rNum = randrange(num)
        new = products[rNum]                            
        return new
    else:
        messagebox.showinfo('Pas de résultat', 'Ce produit semble sain,\n aucune alternative à proposer')
        