import json

def menu():
    print("================== Menu ==================")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
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
    price_input = input("Enter the Price: ")
    stock_input = input("Enter the Stock: ")
    new_product = {"id": id_input, "product": product_input, "price": price_input, "stock": stock_input}
    
    inventory.append(new_product)
    print("Product added successfully.\n")

def save_inventory(inventory):
    with open("Week5/inventory.json", "w") as file:
        json.dump(inventory, file)

def update_stock(inventory):
    product_id = input("Enter the Product ID to update: ")
    new_stock = input("Enter the new stock value: ")
    for item in inventory:
        if item["id"] == product_id:
            item["stock"] = new_stock
            print("Stock updated successfully!\n")
            return
    print(f"Product with ID '{product_id}' not found.\n")

def search_product(inventory):
    search_input = input("Enter the Product ID to search: ")
    for item in inventory:
        if item["id"] == search_input:
            print("================== Product Found ==================")
            print(f"ID: {item['id']}\nProduct: {item['product']}\nPrice: ${item['price']}\nStock: {item['stock']}")
            print("===================================================\n")
            return
    print(f"Product with ID '{search_input}' not found.\n")

inventory = load_inventory()
while True:
    menu()
    menu_input = input("Enter option: ")
    if menu_input == "1":
        display_inventory(inventory)
    elif menu_input == "2":
        add_product(inventory)
        save_inventory(inventory)
    elif menu_input == "3":
        update_stock(inventory)
        save_inventory(inventory)
    elif menu_input == "4":
        search_product(inventory)
    elif menu_input == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")