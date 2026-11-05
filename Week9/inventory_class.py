import json
from physical_product_class import PhysicalProduct
from digital_product_class import DigitalProduct

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
            if item["product_type"] == "physical":
                product = PhysicalProduct(item["id"], item["product"], item["price"], item["stock"], item["weight"])
            elif item["product_type"] == "digital":
                product = DigitalProduct(item["id"], item["product"], item["price"], item["stock"], item["download_size"])

            self.__products.append(product)
        return self.__products

    def save_inventory(self):
        inventory = []
        for product in self.__products:
            if isinstance(product, PhysicalProduct):
                product_data = {
                    "id": product._Product__product_id,
                    "product_type": "physical",
                    "product": product._Product__name,
                    "price": product._Product__price,
                    "stock": product._Product__stock,
                    "weight": product._PhysicalProduct__weight
                }
            elif isinstance(product, DigitalProduct):
                product_data = {
                    "id": product._Product__product_id,
                    "product_type": "digital",
                    "product": product._Product__name,
                    "price": product._Product__price,
                    "stock": product._Product__stock,
                    "download_size": product._DigitalProduct__download_size
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
        product_type = input("Enter the Product Type (physical/digital): ")
        product_input = input("Enter the Product: ")
        price_input = input("Enter the Price: ")
        stock_input = input("Enter the Stock: ")

        if product_type == "physical":
            weight_input = input("Enter the Weight: ")
            new_product = PhysicalProduct(id_input, product_input, float(price_input), int(stock_input), float(weight_input))
        elif product_type == "digital":
            download_size_input = input("Enter the Download Size: ")
            new_product = DigitalProduct(id_input, product_input, float(price_input), int(stock_input), float(download_size_input))

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