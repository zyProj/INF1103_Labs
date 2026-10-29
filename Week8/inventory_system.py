class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        self.__stock += quantity

    def display_information(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock} units")

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product._Product__product_id == product_id:
                return product

    def display_all(self):
        for product in self.__products:
            product.display_information()
            print("=" * 20)

inventory = Inventory()
product1 = Product("P001", "Laptop", 1200.00, 15)
product2 = Product("P002", "Mouse", 25.50, 40)

inventory.add_product(product1)
inventory.add_product(product2)
inventory.display_all()