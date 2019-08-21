

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
        self.products = products
        self.products = products
        self.products = products
        self.products = products
        self.products = products
        self.products = products
        self.products = products
        self.products = products
        self.products = products
        self.products = products
        self.products = products
        self.products = products

    def __repr__(self):
        names = [i for i in self.products['name']]
        return names