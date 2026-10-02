import json

def menu():
    print("================== Menu ==================")
    print("1. Display All Products")
    print("2. Add Product")
    print("6. Exit")
    print("==========================================")

def load_inventory():
    try:
        nested_list = []
        with open("Week5/inventory.json", "r") as file:
            data = json.load(file)
        for item in data:
            nested_list.append({"id": item["id"], "product": item["product"], "price": item["price"], "stock": item["stock"]})
        return nested_list
    
    except FileNotFoundError:
        return []

def display_inventory(inventory):
    print("=====================================================")
    for item in inventory:
        print(f"ID: {item['id']} | Product: {item['product']} | Price: ${item['price']} | Stock: {item['stock']}")
    print("=====================================================\n")

def add_product(inventory):
    id_input = input("Enter the ID: ")
    product_input = input("Enter the Product: ")
    price_input = float(input("Enter the Price: "))
    stock_input = int(input("Enter the Stock: "))
    new_product = {"id": id_input, "product": product_input, "price": price_input, "stock": stock_input}
    
    inventory.append(new_product)
    print("Product added successfully.\n")

def save_inventory(inventory):
    with open("Week5/inventory.json", "w") as file:
        json.dump(inventory, file)

inventory = load_inventory()
while True:
    menu()
    menu_input = input("Enter option: ")
    if menu_input == "1":
        display_inventory(inventory)
    elif menu_input == "2":
        add_product(inventory)
        save_inventory(inventory)
    elif menu_input == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")