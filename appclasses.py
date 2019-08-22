

class User():
    """
    Class used to handle the user creds
    """
    def __init__(self, username, psswd):
        self.username = username
        self.psswd = psswd
        

class AlternativeProduct():
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
        


    def __repr__(self):
        names = [i for i in self.products['name']]
        return names

