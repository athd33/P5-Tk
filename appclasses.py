

class User():
    """
    Class used to handle the user creds
    """
    def __init__(self, login, password):
        self.login = login
        self.password = password


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
        self.other_name = products['product_name']
        self.complement = products['ingredients_text']
        self.portion = products['nutrition_data_prepared_per']
        self.data = products['nutrition_data_prepared_per']
        self.code = products['code']