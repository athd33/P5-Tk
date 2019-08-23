

class User():
    """
    Class used to handle the user creds
    """
    def __init__(self, user_login, user_password):
        self.user_login = user_login
        self.user_password = user_password
        
        

class Product():
    """
    Class used to keep the first category selection
    """
    def __init__(self, products):
        self.products = products
        self.brands = products['brands']
        self.name = products['product_name_fr']
        self.nutriscore = products['nutrition_grades']
        self.url = products['url']
        self.alergen = products['allergens_from_ingredients']
        self.stores = products['stores']
        self.productsName = products['product_name']
        self.ingredients = products['ingredients_text']
        self.data = products['nutrition_data_prepared_per']
        self.code = products['code']
        


