import json

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
    
print(load_inventory())