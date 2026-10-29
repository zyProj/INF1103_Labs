import json

class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id} | Product: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock} units")

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
            with open("Week8/inventory.json", "r") as file:
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
        with open("Week8/inventory.json", "w") as file:
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

inventory = Inventory()
inventory.load_inventory()
while True:
    inventory.menu()
    menu_input = input("Enter option: ")
    if menu_input == "1":
        inventory.display_all()
    elif menu_input == "2":
        inventory.add_product()
        inventory.save_inventory()
    elif menu_input == "3":
        inventory.update_stock()
        inventory.save_inventory()
    elif menu_input == "4":
        inventory.search_product()
    elif menu_input == "5":
        inventory.save_inventory()
        print("Saving Inventory...")
        print("Inventory saved successfully to inventory.json.\n")
    elif menu_input == "6":
        inventory.save_inventory()
        print("Saving Inventory before exit...")
        print("Inventory saved successfully.")
        break
    else:
        print("Invalid option. Please try again.")