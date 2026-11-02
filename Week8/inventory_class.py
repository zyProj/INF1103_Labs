import json
from product_class import Product

class Inventory:
    def __init__(self):
        self.__products = []

    def menu(self):
        print("================== Menu ==================")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("==========================================")

    def load_inventory(self):
        try:
            with open("inventory.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return self.__products

        for item in data:
            product = Product(item["id"], item["product"], item["price"], item["stock"])
            self.__products.append(product)
        return self.__products

    def save_inventory(self):
        inventory = []
        for product in self.__products:
            product_data = {
                "id": product._Product__product_id,
                "product": product._Product__name,
                "price": product._Product__price,
                "stock": product._Product__stock
            }
            inventory.append(product_data)
        with open("inventory.json", "w") as file:
            json.dump(inventory, file)

    def display_all(self):
            print("=====================================================")
            for product in self.__products:
                product.display_information()
            print("=====================================================\n")

    def add_product(self):
        id_input = input("Enter the ID: ")
        product_input = input("Enter the Product: ")
        price_input = input("Enter the Price: ")
        stock_input = input("Enter the Stock: ")
        new_product = Product(id_input, product_input, float(price_input), int(stock_input))
        
        self.__products.append(new_product)
        print("Product added successfully.\n")

    def update_stock(self):
        product_id = input("Enter the Product ID: ")
        quantity = int(input("Enter the Quantity to update: "))
        for product in self.__products:
            if product._Product__product_id == product_id:
                product.update_stock(quantity)
                print("Stock updated successfully.\n")
                return
        print("Product not found.\n")

    def search_product(self):
        product_id = input("Enter the Product ID: ")
        for product in self.__products:
            if product._Product__product_id == product_id:
                product.display_information()
                print("Product found!\n")
                return
        print("Product not found.\n")