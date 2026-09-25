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

print(load_inventory())