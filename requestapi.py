import requests


def category_request():
    req = requests.get('https://fr.openfoodfacts.org/categories&json=1%22')
    responseCode = req.status_code

    if responseCode != 200:
        print(f'Error in request, returned code :{responseCode}')
    else:
        count = 0
        result = req.json()
        tags = result['tags']
        for i in tags:
            count += 1
            print(i['name'])
    print(count)


def aliment_request(num):

   # https://world.openfoodfacts.org/cgi/search.pl?search_terms=vegan&chocolate&search_simple=1&action=process&json=1

    req = requests.get('https://fr-en.openfoodfacts.org/category/pizzas/1.json')
    responseCode = req.status_code

    if responseCode != 200:
        print(f'Error in request, returned code :{responseCode}')
    else:
        count = 0
        result = req.json()
        products = result["products"]
        for i in products:
            count += 1
            stores = i['pnns_groups_2']
            try:
                nutri = i['nutrition_grades']
            except KeyError:
                nutri = 'Information non disponible'
            maj = i['last_edit_dates_tags']
            cat = i['categories']
            
            try:
                store = i['stores']
            except KeyError:
                store = 'Vendeur inconnu'
            try:
                url = i['url']
            except KeyError:
                store = 'Adresse url non disponible'

            
            print(f'Nom :{name}')
            print(f'Catégorie :{cat}')
            print(f'Aliment {count}')
            print(f'Type d\'aliment : {stores} ')
            print(f"Nutriscore : {nutri}")
            print(f'Vendeur : {store}')
            print(f'mise a jour : {maj[0]}')
            print(f'liens : {url}')
            print(' ')
            

def get_aliment_liste(num):
    page = 3
    num -= 1
    aliments = ['pizzas', 'yaourt', 'cookies']
    req = requests.get(f'https://fr-en.openfoodfacts.org/category/{aliments[num]}/5.json')
    responseCode = req.status_code

    if responseCode != 200:
        print(f'Error in request, returned code :{responseCode}')
    else:
        result = req.json()
        products = result["products"]
        return get_products_names(products)
        

def get_products_names(products):
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
