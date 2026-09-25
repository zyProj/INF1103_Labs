def load_inventory():
    with open("Week4/inventory.txt", "r") as file:
        inventory = file.readlines()
    return inventory

print(load_inventory())