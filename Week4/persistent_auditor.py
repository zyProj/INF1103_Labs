def load_inventory():
    try:
        nested_list = []
        with open("Week4/inventory.txt", "r") as file:
            for line in file:
                row = line.strip().split(",")
                nested_list.append(row)
        return nested_list

    except FileNotFoundError:
        return []

def save_inventory(input_list):
    with open("Week4/inventory.txt", "a") as file:
        file.write(input_list[0] + "," + input_list[1] + "," + input_list[2] + "\n")

print("Current Orders:")
for item in load_inventory():
    print(f"{item[0]}: {item[1]} (Quantity: {item[2]})")

while True:
    id_input = input("\nEnter the ID (type 'quit' to exit): ")
    if id_input != "quit":
        product_input = input("Enter the Product: ")
        quantity_input = input("Enter the Quantity: ")
        input_list = [id_input, product_input, quantity_input]

        nested_list = load_inventory()
        nested_list.append(input_list)
        save_inventory(input_list)
    else:
        print("Order successfully saved to inventory.txt")
        break