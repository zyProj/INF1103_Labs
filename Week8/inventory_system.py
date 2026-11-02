from inventory_class import Inventory

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